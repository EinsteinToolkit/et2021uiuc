---
layout: default
usemathjax: true
title: "Numerical Relativity in the Era of Gravitational Wave Astronomy"
author: Deborah Ferguson
institution: The University of Texas at Austin
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
recording: https://youtu.be/ZRLxRvdOGhI
---
{% include base.html %}

{%-capture abstract-%}

Gravitational wave detections have become routine with LIGO and Virgo having announced 50 events to date.
Numerical relativity is crucial for the detection and characterization of each of these binaries.
This talk will discuss the ways gravitational wave detectors use NR waveforms, how we prepare NR waveforms for their use, and what challenges the NR community will need to address to be prepared for the wealth of gravitational wave detections expected in the coming decades.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
