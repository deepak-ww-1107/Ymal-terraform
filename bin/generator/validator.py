import yaml
import re


class ValidationError(Exception):
    pass


class Validator:

    def __init__(self, modules):

        self.modules = modules

    # ----------------------------------------------------
    # Validate YAML
    # ----------------------------------------------------

    def validate(self, yaml_content: str):

        class _MergeDuplicateListKeysLoader(yaml.SafeLoader):
            pass

        def _construct_mapping(loader, node, deep=False):

            mapping = {}

            for key_node, value_node in node.value:

                key = loader.construct_object(key_node, deep=True)
                value = loader.construct_object(value_node, deep=True)

                if key in mapping:

                    existing = mapping[key]

                    if isinstance(existing, list) and isinstance(value, list):

                        mapping[key] = [*existing, *value]

                        continue

                    raise ValidationError(
                        f"Duplicate key '{key}' found in YAML. Use a single key with a list of objects."
                    )

                mapping[key] = value

            return mapping

        _MergeDuplicateListKeysLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            _construct_mapping
        )

        try:
            data = yaml.load(
                yaml_content,
                Loader=_MergeDuplicateListKeysLoader
            )

        except Exception as ex:
            raise ValidationError(
                f"Invalid YAML.\n{str(ex)}"
            )

        if data is None:
            raise ValidationError(
                "YAML file is empty."
            )

        if not isinstance(data, dict):
            raise ValidationError(
                "Root element must be a dictionary."
            )

        reserved_keys = {"agent"}

        module_data = {
            key: value
            for key, value in data.items()
            if key not in reserved_keys
        }

        if not module_data:
            raise ValidationError(
                "No modules found in YAML."
            )

        errors = []

        for module_name, resources in module_data.items():

            # --------------------------------------------
            # Module Exists
            # --------------------------------------------

            if module_name not in self.modules:

                errors.append(
                    f"Unknown module '{module_name}'."
                )

                continue

            terraform_module = self.modules[module_name]

            # --------------------------------------------
            # Module must be list
            # --------------------------------------------

            if not isinstance(resources, list):

                errors.append(
                    f"'{module_name}' must contain a list."
                )

                continue

            # --------------------------------------------
            # Validate each module instance
            # --------------------------------------------

            for index, values in enumerate(resources):

                if not isinstance(values, dict):

                    errors.append(
                        f"{module_name}[{index}] must be an object."
                    )

                    continue

                # Required variables

                for variable in terraform_module.variables.values():

                    if variable.required and variable.name not in values:

                        errors.append(
                            f"{module_name}[{index}] Missing required variable '{variable.name}'."
                        )

                # Unknown variables

                allowed = set(terraform_module.variables.keys())

                for field in values.keys():

                    if field not in allowed:

                        errors.append(
                            f"{module_name}[{index}] Unknown variable '{field}'."
                        )

                # Placeholder validation

                self._validate_placeholders(
                    values,
                    f"{module_name}[{index}]",
                    errors
                )

        if errors:
            raise ValidationError("\n".join(errors))

        return module_data

    # ----------------------------------------------------
    # Validate Placeholder Syntax
    # ----------------------------------------------------

    def _validate_placeholders(self, value, path, errors):

        valid_placeholder = re.compile(
            r"^\$\{[A-Za-z_][A-Za-z0-9_]*\}$"
        )

        if isinstance(value, str):

            if "${" in value and not valid_placeholder.fullmatch(value.strip()):

                errors.append(
                    f"{path} Invalid placeholder '{value}'. Use '${{NAME}}' only (for example: '${{STORAGE_ACCOUNT_ACCESS_KEY}}')."
                )

            return

        if isinstance(value, list):

            for idx, item in enumerate(value):
                self._validate_placeholders(
                    item,
                    f"{path}[{idx}]",
                    errors
                )

            return

        if isinstance(value, dict):

            for key, item in value.items():
                self._validate_placeholders(
                    item,
                    f"{path}.{key}",
                    errors
                )
