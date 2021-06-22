---
layout: default
usemathjax: true
title: LORENE ID I 
author: Maria Babiuc
institution: Marshall University
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

* LORENE ID I

{%-endcapture-%}

{% include lecture.md author=page.author institution=page.institution title=page.title abstract=abstract slides=page.slides files=page.files recording=page.recording%}

