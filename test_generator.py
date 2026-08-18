"""
Unit tests for the model parser and RTL generator.
Run with: pytest tests/ -v
"""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from parser import ModelParser
from generator import RTLGenerator


def test_parser():
    """Model file should load and expose the expected fields."""
    parser = ModelParser('models/simple_reg.yaml')
    model = parser.parse()

    assert model['module_name'] == 'simple_regbank'
    assert len(model['registers']) == 3
    assert model['registers'][0]['name'] == 'control_reg'


def test_parser_validation():
    """Validation should pass for a well-formed model."""
    parser = ModelParser('models/simple_reg.yaml')
    parser.parse()
    assert parser.validate() is True


def test_generator():
    """Generator should render a non-empty Verilog file containing
    the module name and at least one register name."""
    parser = ModelParser('models/simple_reg.yaml')
    model = parser.parse()

    generator = RTLGenerator()
    output = generator.generate('register.v.j2', model)

    assert output.exists()
    content = output.read_text()
    assert len(content) > 0
    assert 'module simple_regbank' in content
    assert 'control_reg' in content


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
