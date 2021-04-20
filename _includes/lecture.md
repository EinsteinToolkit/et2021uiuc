---
---
# {{include.title}}

*{{include.author}} ({{include.institution}})*

**Abstract:** {{include.abstract}}

**slides:** [PDF]({{include.slides}})
{%-if include.files != empty-%}<br>**additional files:**
{% for file in include.files %} [{{file}}]({{file}}){% endfor-%}
{%-endif-%}
{% if include.recording != empty %}<br>**recording:** [mp4]({{include.recording}}){% endif %}
