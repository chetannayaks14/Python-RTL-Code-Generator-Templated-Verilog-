"""
Command-line entry point for the RTL generator.
Usage:
    python main.py models/simple_reg.yaml --template register.v.j2
"""
import argparse
from parser import ModelParser
from generator import RTLGenerator


def main():
    parser = argparse.ArgumentParser(description='RTL Code Generator')
    parser.add_argument('model', help='Path to model file (YAML/JSON)')
    parser.add_argument('--template', default='register.v.j2',
                         help='Template file name')
    parser.add_argument('--output-dir', default='output',
                         help='Output directory')

    args = parser.parse_args()

    # Load and validate the hardware model
    print(f"Parsing model: {args.model}")
    model_parser = ModelParser(args.model)
    model = model_parser.parse()
    model_parser.validate()

    # Render the model into Verilog RTL
    print(f"Generating RTL from template: {args.template}")
    generator = RTLGenerator(output_dir=args.output_dir)
    output_file = generator.generate(args.template, model)

    print(f"Generated: {output_file}")


if __name__ == '__main__':
    main()
