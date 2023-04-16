
default:
	@echo "command      => description"
	@echo "---------------------------"
	@echo "sanitize     => sanitizes all JSON files in data"

sanitize:
	python sanitize_data.py
