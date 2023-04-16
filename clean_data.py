import json
import os


MINIFIED_DIRPATH = "data/minified"
READABLE_DIRPATH = "data/readable"

def main():
	minified_jsons = [os.path.join(MINIFIED_DIRPATH, entry) for entry in os.listdir(MINIFIED_DIRPATH) if entry.endswith(".min.json")]
	for minified_json in minified_jsons:
		with open(minified_json) as f:
			jo = json.load(f)

		with open(minified_json, "w") as f:
			json.dump(jo, f)
		print(f"saved: ({minified_json})")

	readable_jsons = [os.path.join(READABLE_DIRPATH, entry) for entry in os.listdir(READABLE_DIRPATH) if entry.endswith(".json")]
	for readable_json in readable_jsons:
		with open(readable_json) as f:
			jo = json.load(f)

		with open(readable_json, "w") as f:
			json.dump(jo, f, indent="\t")
		print(f"saved: ({readable_json})")


if __name__ == '__main__':
	main()
