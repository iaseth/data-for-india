
# data-for-india

| Code | State | Code | District |
| --- | --- | --- | --- |{% for district in districts %}
| {{ district.stateCode }} | {{ district.state }} | {{ district.districtCode }} | {{ district.district }} |{% endfor %}

