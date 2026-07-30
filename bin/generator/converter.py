from config import Config

from bin.generator.validator import Validator
from bin.generator.template_engine import TemplateEngine
from bin.terraform.module_parser import ModuleParser


class TerraformConverter:

    def __init__(self):

        # -----------------------------------------
        # Load Terraform Modules
        # -----------------------------------------

        self.parser = ModuleParser()

        self.modules = self.parser.load_modules()

        self.validator = Validator(
            self.modules
        )

        self.engine = TemplateEngine(
            self.modules
        )

    # --------------------------------------------------
    # Convert YAML -> Terraform
    # --------------------------------------------------

    def convert(self, yaml_content: str):

        # Validate YAML

        yaml_data = self.validator.validate(
            yaml_content
        )

        # Generate Terraform

        terraform = self.engine.generate(
            yaml_data
        )

        return terraform

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save(

        self,

        terraform: str,

        output_file=Config.GENERATED_MAIN_TF

    ):

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(terraform)
