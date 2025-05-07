---
layout: categories
icon: fas fa-stream
order: 1
---

# Categories

{% for category in site.categories %}
<a href="/categories/{{ category[0] | slugify }}/">{{ category[0] }}</a>
{% endfor %}