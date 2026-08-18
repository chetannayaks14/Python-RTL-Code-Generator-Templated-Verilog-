.PHONY: all install generate test clean view

all: generate

# Set up virtual environment and install dependencies
install:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

# Generate Verilog RTL from the default model/template
generate:
	@echo "Generating RTL..."
	./venv/bin/python src/main.py models/simple_reg.yaml --template register.v.j2
	@echo "Generated: output/simple_regbank.v"

# Run unit tests
test:
	./venv/bin/pytest tests/ -v

# Print the generated Verilog file
view:
	@cat output/simple_regbank.v

# Remove generated output
clean:
	@rm -f output/*.v
	@echo "Cleaned output directory"
