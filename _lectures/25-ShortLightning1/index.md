---
layout: default
usemathjax: true
title: "Short Lightning I"
# list all authors with the names as they appear in the SOC notes (CSV file
# technically)
author:
  - Santiago Jaraba
  - Thiago Assumpção
  - Hayley Macpherson
recordings:
  SantiagoJaraba:
    https://youtu.be/3H3ubJgG5Og
  ThiagoAssumpção:
    https://youtu.be/tKqiSj02yAE
  HayleyMacpherson:
    https://youtu.be/afW2NC8cnRI
---
{% include base.html %}

{% include duration %}
## Short Lighning talk session I

{%assign start = _dur_min_start%}
{% for authorname in page.author %}

{% assign tag = authorname | replace: ' ', '' | replace: '-','' %}
{% assign talk = site.data.lightning | where: 'tag',tag | first %}

<h2 id="{{talk.tag}}">{{forloop.index}}. {{ talk.title }}</h2>
{{start | date: "%I:%M %p"}} -- {{start | plus: 540 | date: "%I:%M %p"}}

<em>{{ talk.name }} ({{ talk.institution }})</em>
{%-assign fn = '/lightning/' | append: talk.tag | append: '.pdf'-%}
{%-assign found = site.static_files | where: "path",fn | first-%}
{%-if found-%}
<a href="{{base}}/lightning/{{talk.tag}}.pdf"> (slides)</a>
{%-endif-%}
{%-if page.recordings[talk.tag]-%}
<a href="{{page.recordings[talk.tag]}}"> (recording)</a>
{%-endif%}

{{ talk.abstract }}

{% assign start = start | plus: 540 %}
{% endfor %}
