import json
import os

import jinja2
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('./templates/')))



def main():
	with open("data/minified/districts.min.json") as f:
		districtsJson = json.load(f)
		districts = districtsJson["districts"]

	readme_md_template = jinja_env.get_template("readme_md.txt")
	readme_text = readme_md_template.render(districts=districts)

	with open("README.md", "w") as f:
		f.write(readme_text)
	print("saved: README.md")

if __name__ == '__main__':
	main()
