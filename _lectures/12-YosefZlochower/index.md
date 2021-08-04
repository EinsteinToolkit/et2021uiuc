---
layout: default
usemathjax: true
title: "SimpleMaxwell: A basic implementation of the Maxwell equations with linear sources"
author: Yosef Zlochower
institution: Rochester Institute of Technlogy
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides:
  - https://github.com/nds-org/jupyter-et/blob/d6026729981802705f1a25aba93f744980b1b4b3/SimpleMaxwell_CactusAndDesignIntro.ipynb
  - https://github.com/nds-org/jupyter-et/blob/d6026729981802705f1a25aba93f744980b1b4b3/SimpleMaxwell_MaxwellSystemAndAlgorithm.ipynb
  - https://github.com/nds-org/jupyter-et/blob/d6026729981802705f1a25aba93f744980b1b4b3/SimpleMaxwell_Parfile.ipynb
recording: https://www.youtube.com/watch?v=uwe1lB04cDI
---
{% include base.html %}

{%-capture abstract-%}
In this tutorial, I will demonstrate how to implement a basic thorn that integrates the Maxwell system with simple linear sources within the Einstein Toolkit.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/d6026729981802705f1a25aba93f744980b1b4b3/{{page.path}})
</div>
