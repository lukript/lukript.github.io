---
layout: tags
icon: fas fa-tags
order: 2
---

# Tags

{% for tag in site.tags %}
<a href="/tags/{{ tag[0] | slugify }}/">{{ tag[0] }}</a>
{% endfor %}
