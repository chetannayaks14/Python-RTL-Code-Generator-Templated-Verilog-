#!/bin/bash
# One-command RTL generation.
# Activates the virtual environment and runs the generator.

echo "========================================="
echo "RTL GENERATOR"
echo "========================================="

source venv/bin/activate

echo "Generating RTL..."
python src/main.py models/simple_reg.yaml --template register.v.j2

echo ""
echo "Done."
ls -lh output/*.v
echo "========================================="
