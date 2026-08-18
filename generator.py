"""
RTL generator that renders a hardware model into Verilog
using a Jinja2 template.
"""
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RTLGenerator:
    """Generate Verilog RTL from a Jinja2 template and a parsed model."""

    def __init__(self, template_dir='templates', output_dir='output'):
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # trim_blocks/lstrip_blocks keep the generated Verilog free of
        # extra blank lines caused by Jinja2 control statements
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def generate(self, template_name, model, output_filename=None):
        """Render the given template with the model data and write it out."""
        template = self.env.get_template(template_name)
        output = template.render(**model)

        if output_filename is None:
            output_filename = f"{model['module_name']}.v"

        output_path = self.output_dir / output_filename
        with open(output_path, 'w') as f:
            f.write(output)

        logger.info(f"Generated: {output_path}")
        return output_path

    def generate_multiple(self, configs):
        """Generate several RTL files from a list of config dictionaries.

        Each config dict should contain: 'template', 'model', and
        optionally 'output' (output filename).
        """
        output_files = []
        for config in configs:
            output_file = self.generate(
                config['template'],
                config['model'],
                config.get('output')
            )
            output_files.append(output_file)
        return output_files
