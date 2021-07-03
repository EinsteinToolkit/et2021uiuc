---
layout: default
usemathjax: true
title: Short Lighting II
# list all authors with the names as they appear in the SOC notes (CSV file
# technically)
author:
  - Jay Vijay Kalinani
  - Dhruv Desai
  - Xinyu Li
  - Atul Kedia
  - Alexandru Dima
---
{% include base.html %}

{% include duration %}
## Short Lighning talk session II

{% for authorname in page.author %}

{% assign tag = authorname | replace: ' ', '' | replace: '-','' %}
{% assign talk = site.data.lightning | where: 'tag',tag | first %}

<h2 id="{{talk.tag}}">{{forloop.index}}. {{ talk.title }}</h2>
<em>{{ talk.name }} ({{ talk.institution }})</em>
{%assign fn = '/lightning/' | append: talk.tag | append: '.pdf'-%}
{%-assign found = site.static_files | where: "path",fn | first-%}
{%-if found-%}
<a href="{{base}}/lightning/{{talk.tag}}.pdf">(slides)</a>
{%-endif%}

{{ talk.abstract }}

{% endfor %}
