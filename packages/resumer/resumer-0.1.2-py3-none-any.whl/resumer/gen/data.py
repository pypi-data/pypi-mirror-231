
import os
import typing
from typing import Any
from pydantic import BaseModel, Field
import tomllib
from resumer.gen.entry import ResumerEntry
from resumer.gen.filter import ResumerFilter
from resumer.gen.key import ResumerKey

class ResumerData(BaseModel):
    simpleKeyData : typing.Dict[str, ResumerKey] = Field(default_factory=dict)
    entryData : typing.List[ResumerEntry] = Field(default_factory=list)
    _registeredTypes : typing.List[str] = Field(exclude=True, kw_only=False)
    extra : dict = Field(default_factory=dict)
    _alreadyParsedLocations : typing.List[str] = Field(exclude=True, kw_only=False)

    def model_post_init(self, __context: Any) -> None:
        self._registeredTypes = []
        self._alreadyParsedLocations = []

    def append(self, **data : dict):
        for k, v in data.items():
            if isinstance(v, list) and all(isinstance(x, dict) for x in v):
                if k not in self._registeredTypes:
                    self._registeredTypes.append(k)

                for entry in v:
                    tags = entry.pop("tags", [])

                    self.entryData.append(ResumerEntry(
                        type_specifier = k,
                        tags = tags,
                        data = entry
                    ))
            else:
                if k in self._registeredTypes:
                    raise ValueError(f"structured key {k} already registered")

                self.simpleKeyData[k] = ResumerKey(
                    key = k,
                    value = v
                )

    def format(self, filter : ResumerFilter):
        preped = {}
        for k, v in self.simpleKeyData.items():
            v.formatData(filter, preped)
        
        for entry in self.entryData:
            entry.formatData(filter, preped)
        
        preped.update(self.extra)

        return preped

    def appendFromPath(self, path : str):
        path = os.path.abspath(path)
        if path in self._alreadyParsedLocations:
            return
        
        self._alreadyParsedLocations.append(path)

        if not os.path.exists(path):
                raise ValueError(f"file {path} does not exist")

        if os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith(".toml"):
                    self.appendFromPath(os.path.join(path, file))

        else:
            with open(path, "rb") as f:
                self.append(**tomllib.load(f))

    @classmethod
    def create(cls, *args):
        rd = cls()
        for arg in args:
            rd.appendFromPath(arg)

        return rd
    
    @classmethod
    def fromConfig(cls, configPath : str, useKey : str = None) -> 'ResumerData':

        if not os.path.exists(configPath):
            raise ValueError(f"config file {configPath} does not exist")
        
        with open(configPath, "rb") as f:
            configData = tomllib.load(f)

        if useKey is not None:
            configData = configData[useKey]

        source = configData.pop("source")

        rd = cls(**configData)

        for path in source:
            rd.appendFromPath(path)

        return rd
        
    @classmethod
    def fromDict(cls, config : dict, useKey : str = None) -> 'ResumerData':
        if useKey is not None:
            config = config[useKey]

        source = config.pop("source")

        rd = cls(**config)

        for path in source:
            rd.appendFromPath(path)

        return rd
        