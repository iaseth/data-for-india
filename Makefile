
default: tasks

tasks:
	@echo "command      => description"
	@echo "---------------------------"
	@echo "readme       => generates README.md"
	@echo "sanitize     => sanitizes all JSON files in data"

readme:
	python generate_readme.py

sanitize:
	python sanitize_data.py
