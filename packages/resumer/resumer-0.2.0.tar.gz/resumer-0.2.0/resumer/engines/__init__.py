
import os
from resumer.engines.base import ResumerEngine as BaseResumerEngine
from resumer.engines.tex import ResumerTexEngine

def get_engine(output : str):
    match os.path.splitext(output)[-1][1:]:
        case "pdf":
            return ResumerTexEngine
        case "tex":
            return ResumerTexEngine
        case _:
            raise ValueError(f"{output} is not a supported output format")
        