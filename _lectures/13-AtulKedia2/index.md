---
layout: default
usemathjax: true
title: LORENE ID
author: Atul Kedia
institution: University of Notre Dame
slides: slides.pdf
<!--files:
  - file1.pdf
  - file2.ipynb
  - file3.mp4-->
recording: ""
---
{% include base.html %}

{%-capture abstract-%}
TBD

* LORENE ID II

{%-endcapture-%}

{% include lecture.md author=page.author institution=page.institution title=page.title abstract=abstract slides=page.slides files=page.files recording=page.recording%}

