from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TerraformVariable:
    """
    Represents one variable inside variables.tf
    """

    name: str
    variable_type: Optional[str] = None
    required: bool = False
    default: Any = None
    description: str = ""


@dataclass
class TerraformOutput:
    """
    Represents one output inside outputs.tf
    """

    name: str
    value: Any = None
    description: str = ""


@dataclass
class TerraformModule:
    """
    Represents one Terraform module.
    """

    name: str

    path: str

    variables: Dict[str, TerraformVariable] = field(default_factory=dict)

    outputs: Dict[str, TerraformOutput] = field(default_factory=dict)


@dataclass
class ModuleInstance:
    """
    Represents one instance of a module from YAML.

    Example

    storage_account:
      - name: stg1
      - name: stg2

    creates

    storage_account_1
    storage_account_2
    """

    module_name: str

    instance_name: str

    values: Dict[str, Any] = field(default_factory=dict)
    index: int = 0


@dataclass
class Dependency:

    variable_name: str

    depends_on_module: str

    output_name: str
