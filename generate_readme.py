import json
import os

import jinja2
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('./templates/')))

datasets = [
	{"filename": "districts", "title": "Districts"},
	{"filename": "stateanimals", "title": "State Animals"},
	{"filename": "statebirds", "title": "State Birds"},
	{"filename": "stateflowers", "title": "State Flowers"},
	{"filename": "statetrees", "title": "State Trees"},
]

def main():
	for dataset in datasets:
		filename = dataset['filename']
		dataset["viewURL"] = f"https://github.com/iaseth/data-for-india/blob/master/data/readable/{filename}.json"
		dataset["rawURL"] = f"https://raw.githubusercontent.com/iaseth/data-for-india/master/data/readable/{filename}.json"
		dataset["rawMinURL"] = f"https://raw.githubusercontent.com/iaseth/data-for-india/master/data/minified/{filename}.min.json"

	with open("data/minified/districts.min.json") as f:
		districtsJson = json.load(f)
		districts = districtsJson["districts"]

	readme_md_template = jinja_env.get_template("readme_md.txt")
	readme_text = readme_md_template.render(
		datasets=datasets,
		districts=districts
	)

	with open("README.md", "w") as f:
		f.write(readme_text)
	print("saved: README.md")

if __name__ == '__main__':
	main()
