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

**slides:**
{% if slideurl-%}
  [PDF]({{slideurl}})
{% else-%}
  N/A
{%-endif-%}

{%-assign files = lectures.files | where_exp: "file", "file.path contains dir" | where_exp: "file", "file.name != slideurl" | where_exp: "file", "file.name != recordingurl" | map: "name" | sort -%}
{%-if files != empty -%}
  <br>**additional files:**
  {% for file in files %} [{{file | split: "/" | last}}]({{file | split: "/" | last}}){% endfor-%}
{%-endif-%}

<br>**recording:**
{% if recordingurl-%}
  [mp4]({{recordingurl}})
{% else-%}
  N/A
{%-endif-%}
