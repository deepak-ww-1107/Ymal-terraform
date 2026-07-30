from jinja2 import Environment, FileSystemLoader
import re

from config import Config
from bin.generator.utils import TerraformFormatter


class TemplateEngine:

    def __init__(self, modules):

        self.modules = modules

        self.environment = Environment(
            loader=FileSystemLoader(Config.TEMPLATE_DIR),
            trim_blocks=True,
            lstrip_blocks=True
        )

        self.template = self.environment.get_template(
            "module.j2"
        )

    # ---------------------------------------------------------
    # Generate Terraform
    # ---------------------------------------------------------

    def generate(self, yaml_data):

        terraform = []
        placeholder_variables = set()

        for module_name, resources in yaml_data.items():

            module = self.modules.get(module_name)

            for index, resource in enumerate(resources):

                values = {}

                for key, value in resource.items():

                    variable_type = None

                    if module and key in module.variables:

                        variable_type = module.variables[key].variable_type

                    coerced_value = self._coerce_value_by_type(
                        value,
                        variable_type
                    )

                    self._collect_placeholder_variables(
                        coerced_value,
                        placeholder_variables
                    )

                    values[key] = TerraformFormatter.format(coerced_value)

                terraform.append(

                    self.template.render(

                        instance_name=f"{module_name}_{index + 1}",

                        module_name=module_name,

                        variables=values

                    )

                )

        terraform_body = "\n\n".join(terraform)

        if not placeholder_variables:
            return terraform_body

        declarations = []

        for variable_name in sorted(placeholder_variables):

            declarations.append(
                f'variable "{variable_name}" {{\n'
                f'  type = string\n'
                f'}}'
            )

        return "\n\n".join([*declarations, terraform_body])

    # ---------------------------------------------------------
    # Coerce YAML value by Terraform variable type
    # ---------------------------------------------------------

    def _coerce_value_by_type(self, value, variable_type):

        if not isinstance(variable_type, str):
            return value

        normalized_type = variable_type.strip().lower().replace(" ", "")

        if normalized_type.startswith("${") and normalized_type.endswith("}"):
            normalized_type = normalized_type[2:-1]

        if not normalized_type.startswith("map("):
            return value

        if not isinstance(value, list):
            return value

        map_value = {}

        for item in value:

            if not isinstance(item, dict):
                return value

            item_key = item.get("key")

            if not isinstance(item_key, str) or not item_key.strip():
                return value

            map_value[item_key] = item.get("value")

        return map_value

    # ---------------------------------------------------------
    # Collect ${NAME} placeholders
    # ---------------------------------------------------------

    def _collect_placeholder_variables(self, value, placeholders):

        if isinstance(value, str):

            match = re.fullmatch(
                r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}",
                value.strip()
            )

            if match:
                placeholders.add(match.group(1))

            return

        if isinstance(value, list):

            for item in value:
                self._collect_placeholder_variables(item, placeholders)

            return

        if isinstance(value, dict):

            for item in value.values():
                self._collect_placeholder_variables(item, placeholders)
