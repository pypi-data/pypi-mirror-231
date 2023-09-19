
from resumer.engines.base import ResumerEngine
from resumer.utils import check_installed
import os
import typing

class ResumerTexEngine(ResumerEngine):
    includeDir : str = None
    output : str = "output/output.pdf"

    def _generate_pdf(self, output : str):
        if not check_installed("xelatex"):
            raise RuntimeError("xelatex is not installed")
        
        cmd = f"xelatex {output} -output-directory={os.path.dirname(output)}"

        if self.includeDir:
            cmd += f" -include-directory={self.includeDir}"

        os.system(cmd)


    def generate(self, output: str, data: dict):
        if output is None:
            output = self.output

        if output.endswith(".pdf"):
            gen_pdf = True
            tex_output = output.replace(".pdf", ".tex")
        else:
            gen_pdf = False
            tex_output = output
        
        super().generate(tex_output, data)
        
        if not gen_pdf:
            return
        
        self._generate_pdf(tex_output)

        self.lastGenerated = output