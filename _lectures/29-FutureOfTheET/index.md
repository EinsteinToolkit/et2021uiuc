---
layout: default
usemathjax: true
title: Future of the Einstein Toolkit
author: Roland Haas
institution: The University of Illinois Urbana Champaign
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

* Numerical Relativity

{{page.duration}}

{%-endcapture-%}

{% include lecture.md author=page.author institution=page.institution title=page.title abstract=abstract slides=page.slides files=page.files recording=page.recording%}

