---
layout: default
usemathjax: true
title: "Binary Neutron Star ID construction with LORENE"
author: Atul Kedia
institution: University of Notre Dame
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: Atul-LORENE talk.pptx
recording: https://youtu.be/-NUD-piBeek
---
{% include base.html %}

{%-capture abstract-%}
In this tutorial style lecture, we will learn how to use LORENE to generate Binary Neutron Star (BNS) Initial Data (ID). We will discuss how to use the different Equations of state (EoS) formats acceptable to LORENE and perform necessary unit conversions. Further, we will discuss the process of forming Piecewise Polytropic EoSs. The commands to generate ID on the tutorial server can be found in the last slide of the PPTX file below.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
