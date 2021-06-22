---
layout: default
usemathjax: true
title: Spritz
author: Federico Cipolletta
institution: Rochester Institute of Technology
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

* Spritz



{%-endcapture-%}

{% include lecture.md author=page.author institution=page.institution title=page.title abstract=abstract slides=page.slides files=page.files recording=page.recording%}

