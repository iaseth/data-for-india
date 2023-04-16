
# data-for-india
This repository contains JSON datasets that might be useful for making applications for Indian users.


## List of datasets

| Dataset | View | Download | Minified |
| --- | --- | --- | --- |{% for dataset in datasets %}
| {{ dataset["title"] }} | [View]({{ dataset["viewURL"] }}) | [Download]({{ dataset["rawURL"] }}) | [Download]({{ dataset["rawMinURL"] }}) |{% endfor %}


## List of districts

| Code | State | Code | District |
| --- | --- | --- | --- |{% for district in districts %}
| {{ district.stateCode }} | {{ district.state }} | {{ district.districtCode }} | {{ district.district }} |{% endfor %}

