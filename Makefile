
default: tasks

tasks:
	@echo "command      => description"
	@echo "---------------------------"
	@echo "build        => builds the package with tsc"
	@echo "readme       => generates README.md"
	@echo "sanitize     => sanitizes all JSON files in data"

lint:
	npm run lint

build:
	npm run build

readme:
	python generate_readme.py

sanitize:
	python sanitize_data.py
