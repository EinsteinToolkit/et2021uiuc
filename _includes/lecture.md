{% include duration %}

# {{page.title}}

*{{page.author}} ({{page.institution}})*

**Abstract:** {{include.abstract}}

{% comment-%}page.dir returns the empty string for me{%-endcomment-%}
{%-assign dir = page.path | split: '/' | pop | join: "/" | append: "/"-%}
{%-comment-%}somehow this is different from site.lectures and contains the .files member I want{%-endcomment-%}
{%-assign lectures = site.collections | where: "label", "lectures" | first-%}

{%-if page.slides-%}
  {%-assign slideurl = page.slides-%}
{%-else-%}
  {%-assign fn = dir | append: "slides.pdf"-%}
  {%-assign found = lectures.files | where: "path", fn | first-%}
  {%-if found-%}
  {%-assign slideurl = "slides.pdf"-%}
  {%-else-%}
  {%-assign slideurl = nil-%}
  {%-endif-%}
{%-endif-%}

{%-if page.recording-%}
  {%-assign recordingurl = page.recording-%}
{%-else-%}
  {%-assign fn = dir | append: "recording.mp4"-%}
  {%-assign found = lectures.files | where: "path", fn | first-%}
  {%-if found-%}
  {%-assign recordingurl = "recording.mp4"-%}
  {%-else %}
  {%-assign recordingurl = nil-%}
  {%-endif-%}
{%-endif-%}

<div style="text-align: left">
<strong>slides:</strong>
{% if slideurl-%}
  {%-for url in slideurl %} <a href="{{url}}">{{url | split: '/' | last}}</a>{% endfor-%}
{% else-%}
  N/A
{% endif %}
</div>

{% assign files = lectures.files | where_exp: "file", "file.path contains dir" | where_exp: "file", "file.name != slideurl" | where_exp: "file", "file.name != recordingurl" | map: "name" | sort -%}
{%-if files != empty %}
<div style="text-align: left">
  <strong>additional files:</strong>
  {% for file in files %} <a href="{{file | split: "/" | last}}">{{file | split: "/" | last}}</a>{% endfor-%}
</div>
{% endif %}

<div style="text-align: left">
<strong>recording:</strong>
{% if recordingurl-%}
  <a href="{{recordingurl}}">watch</a>
{% else-%}
  N/A
{%-endif-%}
</div>
