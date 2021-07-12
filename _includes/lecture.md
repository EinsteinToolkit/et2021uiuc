{% include duration %}

# {{page.title}}

*{{page.author}} ({{page.institution}})*

**Abstract:** {{include.abstract}}

{% comment-%}page.dir returns the empty string for me{%-endcomment-%}
{%-assign dir = page.path | split: '/' | pop | join: "/" | append: "/"-%}
{%-comment-%}somehow this is different from site.lectures and contains the .files member I want{%-endcomment-%}
{%-assign lectures = site.collections | where: "label", "lectures" | first-%}

**slides:**
{%-assign fn = dir | append: "slides.pdf"-%}
{%-assign found = lectures.files | where: "path", fn | first-%}
{%-if found %}
  [PDF](slides.pdf)
{%-else %}
  N/A
{%-endif-%}

{%-assign files = lectures.files | where_exp: "file", "file.path contains dir" | where_exp: "file", "file.name != 'slides.pdf'" | where_exp: "file", "file.name != 'recording.mp4'" | map: "name" | sort -%}
{%-if files != empty -%}
  <br>**additional files:**
  {% for file in files %} [{{file | split: "/" | last}}]({{file | split: "/" | last}}){% endfor-%}
{%-endif-%}

<br>**recording:**
{%-if page.recording %}
  [mp4]({{page.recording}})
{%-else %}
  {%-assign fn = dir | append: "recording.mp4"-%}
  {%-assign found = lectures.files | where: "path", fn | first-%}
  {%-if found %}
  [mp4](recording.mp4)
  {%-else %}
  N/A
  {%-endif-%}
{%-endif %}
