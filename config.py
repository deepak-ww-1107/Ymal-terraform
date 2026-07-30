from pathlib import Path


class Config:
    """
    Application Configuration
    """

    # ---------------------------------------
    # Root Directory
    # ---------------------------------------

    ROOT_DIR = Path(__file__).resolve().parent

    # ---------------------------------------
    # Project Folders
    # ---------------------------------------

    MODULES_DIR = ROOT_DIR / "modules"

    TEMPLATE_DIR = ROOT_DIR / "bin" / "templates"

    OUTPUT_DIR = ROOT_DIR / "output"

    # ---------------------------------------
    # Output Files
    # ---------------------------------------

    GENERATED_MAIN_TF = OUTPUT_DIR / "main.tf"

    # ---------------------------------------
    # Generic Template
    # ---------------------------------------

    MODULE_TEMPLATE = TEMPLATE_DIR / "module.j2"

    # ---------------------------------------
    # File Names
    # ---------------------------------------

    VARIABLES_FILE = "variables.tf"

    OUTPUTS_FILE = "outputs.tf"

    MAIN_FILE = "main.tf"

    # ---------------------------------------
    # Supported Extensions
    # ---------------------------------------

    YAML_EXTENSIONS = [".yaml", ".yml"]

    # ---------------------------------------
    # Create Output Folder Automatically
    # ---------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )