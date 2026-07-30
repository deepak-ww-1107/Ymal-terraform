import json
import re


class TerraformFormatter:
    """
    Converts Python values into valid Terraform syntax.
    """

    @staticmethod
    def format(value):

        # --------------------------------------------------
        # None
        # --------------------------------------------------

        if value is None:
            return "null"

        # --------------------------------------------------
        # Boolean
        # --------------------------------------------------

        if isinstance(value, bool):
            return str(value).lower()

        # --------------------------------------------------
        # Number
        # --------------------------------------------------

        if isinstance(value, (int, float)):
            return str(value)

        # --------------------------------------------------
        # String
        # --------------------------------------------------

        if isinstance(value, str):

            placeholder_match = re.fullmatch(
                r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}",
                value.strip()
            )

            if placeholder_match:
                return f"var.{placeholder_match.group(1)}"

            # Terraform References

            if value.startswith("module."):
                return value

            if value.startswith("data."):
                return value

            if value.startswith("var."):
                return value

            if value.startswith("local."):
                return value

            return json.dumps(value)

        # --------------------------------------------------
        # List
        # --------------------------------------------------

        if isinstance(value, list):

            values = []

            for item in value:

                values.append(

                    TerraformFormatter.format(item)

                )

            return "[{}]".format(

                ", ".join(values)

            )

        # --------------------------------------------------
        # Dictionary
        # --------------------------------------------------

        if isinstance(value, dict):

            output = "{\n"

            for key, item in value.items():

                output += (
                    f"  {key} = "
                    f"{TerraformFormatter.format(item)}\n"
                )

            output += "}"

            return output

        return json.dumps(str(value))

    # ------------------------------------------------------
    # Detect Terraform Expression
    # ------------------------------------------------------

    @staticmethod
    def is_expression(value):

        if not isinstance(value, str):
            return False

        expressions = (

            "module.",

            "var.",

            "data.",

            "local."

        )

        return value.startswith(expressions)

    # ------------------------------------------------------
    # Format List
    # ------------------------------------------------------

    @staticmethod
    def format_list(values):

        output = []

        for value in values:

            output.append(

                TerraformFormatter.format(value)

            )

        return "[{}]".format(

            ", ".join(output)

        )

    # ------------------------------------------------------
    # Format Map
    # ------------------------------------------------------

    @staticmethod
    def format_map(values):

        output = "{\n"

        for key, value in values.items():

            output += (
                f"  {key} = "
                f"{TerraformFormatter.format(value)}\n"
            )

        output += "}"

        return output
