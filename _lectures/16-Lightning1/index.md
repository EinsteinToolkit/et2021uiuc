---
layout: default
usemathjax: true
title: Lighting I
author: TBD
institution: 
slides: slides.pdf
files:
  - file1.pdf
  - file2.ipynb
  - file3.mp4
recording: ""
---
{% include base.html %}

{%-capture abstract-%}
TBD

* GW wave analysis
* eggs

and use $$\LaTeX$$ to display

$$\begin{equation}E = m c^2\end{equation}$$
{%-endcapture-%}

{% include lecture.md author=page.author institution=page.institution title=page.title abstract=abstract slides=page.slides files=page.files recording=page.recording%}

Anything else that should appear after the "front matter" stuff above.
