---
layout: default
usemathjax: true
title: "Tutorial: 3+1 decomposition with xTensor"
author: Helvi Witek
institution: University of Illinois Urbana-Champaign
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: GR_Split.nb
recording: https://youtu.be/Bt5iybdofgw
---
{% include base.html %}

{%-capture abstract-%}
The open-source xAct suite is a powerful tool for tensor algebra with Mathematica, and its xTensor package is particularly useful for abstract tensor computations. In this tutorial, we will use xTensor to derive the ADM-York equations for Einstein's equations.

To run the tutorial on your own laptop, please install the xAct package before class; see [xAct.es](http://www.xact.es)
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
