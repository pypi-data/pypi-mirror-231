
from abc import abstractmethod
import os
from pydantic import BaseModel, Field
import yaml
import tomllib
from resumer.utils import check_installed, rename_bkup

class ResumerEngine(BaseModel):
    template : str
    tempInputData : str = "temp/input.md"
    output : str = None
    extra : dict = Field(default_factory=dict)
    lastGenerated : str = None

    @classmethod
    def fromDict(cls, config : dict, useKey : str = None):
        if useKey is not None:
            config = config[useKey]

        return cls(**config)
    
    @classmethod
    def fromConfig(cls, configPath : str, useKey : str = None):
        with open(configPath, "rb") as f:
            configData = tomllib.load(f)
        
        if useKey is not None:
            configData = configData[useKey]
        
        return cls(**configData)


    @property
    def template_extension(self):
        return os.path.splitext(self.template)[-1][1:]
    
    @property
    def template_type(self):
        match self.template_extension:
            case "md":
                return "markdown"
            case "tex":
                return "latex"
            case _:
                return self.template_extension
            

    @staticmethod
    def _write_yaml(data : dict, path : str):
        yaml_data = yaml.dump(data)
        with open(path, "w") as f:
            f.write("---\n")
            f.write(yaml_data)
            f.write("---\n")


    def _generate_input(self, data : dict, **kwargs):
        dir_path = os.path.dirname(self.tempInputData)
        os.makedirs(dir_path, exist_ok=True)

        rename_bkup(self.tempInputData)

        ResumerEngine._write_yaml(data, self.tempInputData)
        return self.tempInputData
        
    @abstractmethod
    def generate(self, output : str, data : dict):
        if output is None:
            output = self.output

        if not check_installed("pandoc"):
            raise RuntimeError("pandoc is not installed")

        path = self._generate_input(data)

        os.system(
            f'pandoc "{path}" -o "{output}" -f markdown -t latex --template="{self.template}"'
        )

        self.lastGenerated = output

    def openLastGenerated(self):
        if self.lastGenerated:
            cwd = os.getcwd()
            os.startfile(os.path.join(cwd, self.lastGenerated))
