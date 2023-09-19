
import typing
from resumer.gen.base import BaseResumerUnit
from resumer.gen.filter import ResumerFilter
from pydantic import dataclasses

from resumer.utils import get_drill_vars, rough_check_drill_string

@dataclasses.dataclass
class ResumerKey(BaseResumerUnit):
    key : str
    value : typing.Any

    def _process_drill(self, filter : ResumerFilter) -> typing.Any:
        if not isinstance(self.value, str):
            return self.value
        
        if not rough_check_drill_string(self.value):
            return self.value

        res = get_drill_vars(self.value)

        if res is None:
            return self.value
        
        var_details, raw_string = res
        
        format_vars = {k : "" for k in var_details}

        for k, v in var_details.items():
            if filter.drill_match(k):
                format_vars[k] = v

        return raw_string.format(**format_vars)

    def formatData(self, filter: ResumerFilter, data: dict):
        if filter is None:
            data[self.key] = self.value
            return

        if filter.direct_match(self.key):
            data[self.key] = self._process_drill(filter)

        return data