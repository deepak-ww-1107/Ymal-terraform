from pathlib import Path
from typing import Dict

import hcl2

from config import Config
from bin.terraform.models import (
    TerraformModule,
    TerraformVariable,
    TerraformOutput
)


class ModuleParser:

    def __init__(self):

        self.modules: Dict[str, TerraformModule] = {}

    # =====================================================
    # PUBLIC
    # =====================================================

    def load_modules(self):

        self.modules.clear()

        if not Config.MODULES_DIR.exists():
            raise Exception(
                f"Modules folder not found : {Config.MODULES_DIR}"
            )

        for folder in Config.MODULES_DIR.iterdir():

            if not folder.is_dir():
                continue

            module = TerraformModule(
                name=folder.name,
                path=str(folder)
            )

            module.variables = self._read_variables(folder)

            module.outputs = self._read_outputs(folder)

            self.modules[module.name] = module

        return self.modules

    def get_modules(self):

        return self.modules

    def get_module(self, module_name):

        return self.modules.get(module_name)

    # =====================================================
    # VARIABLES
    # =====================================================

    def _read_variables(self, module_path: Path):

        variables = {}

        file = module_path / Config.VARIABLES_FILE

        if not file.exists():
            return variables

        with open(file, "r", encoding="utf-8") as f:

            data = hcl2.load(f)

        for variable in data.get("variable", []):

            for name, body in variable.items():

                variables[name] = TerraformVariable(

                    name=name,

                    variable_type=str(
                        body.get("type", "any")
                    ),

                    required="default" not in body,

                    default=body.get("default"),

                    description=body.get(
                        "description",
                        ""
                    )

                )

        return variables

    # =====================================================
    # OUTPUTS
    # =====================================================

    def _read_outputs(self, module_path: Path):

        outputs = {}

        file = module_path / Config.OUTPUTS_FILE

        if not file.exists():
            return outputs

        with open(file, "r", encoding="utf-8") as f:

            data = hcl2.load(f)

        for output in data.get("output", []):

            for name, body in output.items():

                outputs[name] = TerraformOutput(

                    name=name,

                    value=body.get("value"),

                    description=body.get(
                        "description",
                        ""
                    )

                )

        return outputs

    # =====================================================
    # OUTPUT MATCHING
    # =====================================================

    def find_best_output(

        self,

        module_name: str,

        variable_name: str

    ):

        """
        Example

        storage_account_access_key

        ↓

        primary_access_key

        """

        module = self.modules.get(module_name)

        if module is None:
            return None

        outputs = module.outputs

        if not outputs:
            return None

        # -----------------------------------------
        # Exact Match
        # -----------------------------------------

        if variable_name in outputs:

            return variable_name

        # -----------------------------------------
        # Remove Module Prefix
        # -----------------------------------------

        remaining = variable_name

        if remaining.startswith(module_name + "_"):

            remaining = remaining[len(module_name) + 1:]

        # Exact

        if remaining in outputs:

            return remaining

        # -----------------------------------------
        # Contains Match
        # -----------------------------------------

        for output in outputs.keys():

            if remaining in output:

                return output

        # -----------------------------------------
        # Reverse Contains
        # -----------------------------------------

        for output in outputs.keys():

            if output in remaining:

                return output

        return None
