
import typing
from pydantic import Field
from resumer.gen.base import BaseResumerUnit
from pydantic import dataclasses

from resumer.gen.filter import ResumerFilter
from resumer.utils import get_drill_vars, rough_check_drill_string

@dataclasses.dataclass
class ResumerEntry(BaseResumerUnit):
    type_specifier : str
    data : dict
    tags : typing.List[str] = Field(default_factory=list)
    
    def _format_drill(self, raw_string : str, filter : ResumerFilter):
        if not rough_check_drill_string(raw_string):
            return raw_string

        res = get_drill_vars(raw_string)

        if res is None:
            return raw_string
        
        var_details, base_string = res
        
        format_vars = {x : "" for x in var_details}

        for a, b in var_details.items():
            if filter.drill_match(a):
                format_vars[a] = b

        return base_string.format(**format_vars)

    def _process_drill(self, filter: ResumerFilter):
        copied_data = self.data.copy()
        pending_deletions = []

        for k, v in copied_data.items():
            if isinstance(v, list):
                for vi, vitem in enumerate(v):
                    res = self._format_drill(vitem, filter)
                    copied_data[k][vi] = res

                copied_data[k] = [vitem for vitem in v if vitem]
                
            elif isinstance(v, dict):
                for k2, v2 in v.items():
                    copied_data[k][k2] = self._format_drill(v2, filter)
                copied_data[k] = {k2 : v2 for k2, v2 in v.items() if v2}

            elif isinstance(v, str):
                copied_data[k] = self._format_drill(v, filter)
                if not copied_data[k]:
                    pending_deletions.append(k)

            else:
                continue

        return {k : v for k, v in copied_data.items() if k not in pending_deletions}
    
    def _appenddata(self, data : dict, filter : ResumerFilter):
        if self.type_specifier not in data:
            data[self.type_specifier] = []

        if filter is not None:
            drilled_data = self._process_drill(filter)
        else:
            drilled_data = self.data

        data[self.type_specifier].append(drilled_data)

        return data

    def formatData(self, filter: ResumerFilter, data: dict):
        if filter is None:
            return self._appenddata(data, filter)

        structured_res = filter.structured_matches(self.tags, self.type_specifier)
        if structured_res:
            return self._appenddata(data, filter)
        
        if structured_res is False:
            return data
        
        direct_res = filter.direct_matches(self.tags)
        if not direct_res:
            return data
        
        return self._appenddata(data, filter)
    

            