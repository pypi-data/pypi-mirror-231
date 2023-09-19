
from functools import cached_property
import typing
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, model_validator


class ResumerFilter(BaseModel):
    includes : typing.List[str] = Field(default_factory=list)
    excludes : typing.List[str] = Field(default_factory=list)
    drillExIncludes : typing.List[str] = Field(default_factory=list)
    drillExExcludes : typing.List[str] = Field(default_factory=list)

    def model_post_init(self, __context: Any) -> None:
        for include in self.includes.copy():
            if include.startswith("^"):
                self.drillExIncludes.append(include[1:])
                self.includes.remove(include)

        for exclude in self.excludes.copy():
            if exclude.startswith("^"):
                self.drillExExcludes.append(exclude[1:])
                self.excludes.remove(exclude)

        if any("." in include for include in self.drillExIncludes):
            raise ValueError("drillExIncludes cannot contain '.'")

        if any("." in exclude for exclude in self.drillExExcludes):
            raise ValueError("drillExExcludes cannot contain '.'")

    model_config = ConfigDict(
        ignored_types=(cached_property,)
    )

    @model_validator(mode="after")
    def _validate_model(self):
        # make sure includes and excludes have no same keys
        for key in self.includes:
            if key in self.excludes:
                raise ValueError(f"includes and excludes cannot have same keys: {key}")
            
        return self

    @cached_property
    def direct_includes(self):
        sin = []
        for tag in self.includes:
            if "." in tag:
                continue
            sin.append(tag)
            
        return sin

    @cached_property
    def direct_excludes(self):
        sex = []
        for tag in self.excludes:
            if "." in tag:
                continue
            sex.append(tag)
            
        return sex
    
    @cached_property
    def structured_includes(self):
        sin = {}
        for tag in self.includes:
            if "." not in tag:
                continue

            tag_parts = tag.split(".", 1)

            if tag_parts[0] not in sin:
                sin[tag_parts[0]] = []
            sin[tag_parts[0]].append(tag_parts[1])

        return sin
    
    @cached_property
    def structured_excludes(self):
        sex = {}
        for tag in self.excludes:
            if "." not in tag:
                continue

            tag_parts = tag.split(".", 1)

            
            if tag_parts[0] not in sex:
                sex[tag_parts[0]] = []
            sex[tag_parts[0]].append(tag_parts[1])

        return sex

    @cached_property
    def no_filters(self):
        return len(self.direct_includes) == 0 and len(self.direct_excludes) == 0

    @cached_property
    def no_drill_filters(self):
        return len(self.drillExIncludes) == 0 and len(self.drillExExcludes) == 0

    def direct_match(self, key : str):
        if "." in key:
            raise ValueError

        if self.no_filters:
            return True
        
        if key in self.direct_includes:
            return True
        
        if key in self.direct_excludes:
            return False
        
        if len(self.direct_includes) == 0 and key not in self.direct_excludes:
            return True
        
        if len(self.direct_excludes) == 0 and key not in self.direct_includes:
            return False
        
        return len(self.direct_includes) == 0
    
    def direct_matches(self, keys : typing.List[str]):
        if any("." in key for key in keys):
            raise ValueError
        
        if self.no_filters:
            return True
        
        empty_includes = len(self.direct_includes) == 0
        empty_excludes = len(self.direct_excludes) == 0

        if all(key for key in keys if key in self.direct_includes) and not empty_includes and not empty_excludes:
            return True
        
        if any(key for key in keys if key in self.direct_excludes) and not empty_excludes and not empty_includes:
            return False
            
        if(
            len(self.direct_excludes) == 0
            and any(key for key in keys if key not in self.direct_includes)
        ):
            return True
        
        if(
            len(self.direct_includes) == 0
            and any(key for key in keys if key not in self.direct_excludes)
        ):
            return False

        return len(self.direct_includes) == 0

    def drill_match(self, key : str):
        if key in self.drillExIncludes:
            return True
        
        if key in self.drillExExcludes:
            return False

        return self.direct_match(key)

    def structured_match(self, key : str, type_specifier : str):
        if "." in key:
            raise ValueError

        if self.no_filters:
            return True

        target_includes = self.structured_includes.get(type_specifier, [])
        target_excludes = self.structured_excludes.get(type_specifier, [])

        if key in target_includes:
            return True
        
        if key in target_excludes:
            return False
        
        if (
            len(self.structured_includes) == 0 
            and key not in target_excludes
        ):
            return True
        
        if (
            len(self.structured_excludes) == 0
            and key not in target_includes
        ):
            return False

        return len(target_includes) == 0

    def structured_matches(self, keys : typing.List[str], type_specifier : str):
        if any("." in key for key in keys):
            raise ValueError
        
        if self.no_filters:
            return True
        
        includes = self.structured_includes.get(type_specifier, [])
        excludes = self.structured_excludes.get(type_specifier, [])
        empty_includes = len(includes) == 0
        empty_excludes = len(excludes) == 0                   

        if all(key for key in keys if key in includes) and not empty_includes and empty_excludes:
            return True
        
        if any(key for key in keys if key in excludes) and not empty_excludes and empty_includes:
            return False
        
        if empty_includes and any(key for key in keys if key not in excludes):
            return False
        
        if empty_excludes and any(key for key in keys if key not in includes):
            return True
        
        return empty_includes
