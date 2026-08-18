"""
YAML/JSON parser for hardware register models.
Loads a hardware specification file and validates its structure
before it is passed to the RTL generator.
"""
import yaml
import json
from pathlib import Path


class ModelParser:
    """Parse hardware specification from YAML or JSON."""

    def __init__(self, model_path):
        self.model_path = Path(model_path)
        self.model = None

    def parse(self):
        """Load and parse the model file based on its extension."""
        if self.model_path.suffix in ['.yaml', '.yml']:
            with open(self.model_path, 'r') as f:
                self.model = yaml.safe_load(f)
        elif self.model_path.suffix == '.json':
            with open(self.model_path, 'r') as f:
                self.model = json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {self.model_path.suffix}")

        return self.model

    def validate(self):
        """Check that the model has the minimum required fields."""
        required_keys = ['module_name', 'registers']
        for key in required_keys:
            if key not in self.model:
                raise ValueError(f"Missing required key: {key}")

        # Every register must at least have a name and an address
        for reg in self.model['registers']:
            if 'name' not in reg or 'address' not in reg:
                raise ValueError("Register missing name or address")

        return True
