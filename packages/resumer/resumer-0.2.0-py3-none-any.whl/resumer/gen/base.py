

import typing
from resumer.gen.filter import ResumerFilter
from pydantic import dataclasses

@dataclasses.dataclass
class BaseResumerUnit:
    def _process_drill(self, filter : ResumerFilter) -> typing.Any:
        raise NotImplementedError

    def formatData(self, filter : ResumerFilter, data : dict):
        raise NotImplementedError
    