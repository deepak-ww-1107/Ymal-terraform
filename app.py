import argparse
import sys
from pathlib import Path

import yaml

from config import Config
from bin.generator.converter import TerraformConverter


def _read_yaml_content(input_file: str | None) -> str:

    if input_file:

        with open(input_file, "r", encoding="utf-8") as file:

            return file.read()

    if not sys.stdin.isatty():

        return sys.stdin.read()

    raise ValueError(
        "Provide a YAML file path with --input or pipe YAML through stdin."
    )


def _extract_agent_name(yaml_content: str) -> str:

    try:

        data = yaml.safe_load(yaml_content)

    except Exception as ex:

        raise ValueError(f"Invalid YAML. {ex}")

    if not isinstance(data, dict):

        raise ValueError("Root element must be a dictionary.")

    agent = data.get("agent")

    if not isinstance(agent, str) or not agent.strip():

        raise ValueError("YAML must include a non-empty 'agent' field.")

    return agent.strip()


def _derive_output_path(
    input_file: str | None,
    explicit_output: str | None,
) -> str:

    if explicit_output:

        return explicit_output

    if input_file:

        input_path = Path(input_file).resolve()

        return str(input_path.parent / "output" / "main.tf")

    return str(Config.GENERATED_MAIN_TF)


def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Generate Terraform from YAML module definitions."
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        help="Path to the YAML input file.",
    )

    parser.add_argument(
        "-i",
        "--input",
        help="Path to the YAML input file. If omitted, YAML is read from stdin.",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Path to the generated Terraform file.",
    )

    return parser.parse_args()


def main() -> int:

    args = parse_args()

    input_file = args.input or args.input_file

    yaml_content = _read_yaml_content(input_file)

    agent_name = _extract_agent_name(yaml_content)

    output_file = _derive_output_path(input_file, args.output)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    converter = TerraformConverter()

    terraform = converter.convert(yaml_content)

    converter.save(terraform, output_file)

    print(f"Agent: {agent_name}")

    print(f"Terraform generated successfully: {output_file}")

    return 0


# -------------------------------------------------------
# Main
# -------------------------------------------------------

if __name__ == "__main__":

    try:

        raise SystemExit(main())

    except Exception as ex:

        print(f"Error: {ex}", file=sys.stderr)

        raise SystemExit(1)