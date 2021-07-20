---
layout: default
usemathjax: true
title: "NRPy+ tutorial: gravitational collapse of massless scalar fields"
author: Leonardo Werneck
institution: West Virginia University
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explicit URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
The 2020 Einstein Toolkit workshop had a NRPy+ tutorial on how to
implement the wave equation in flat space (you can re-watch the
tutorial given by Zach Etienne [here](https://www.youtube.com/watch?v=TIPiW5-mPOM)).
In this tutorial, we present the natural next step by describing how to use
NRPy+ to implement the Klein-Gordon equations for a massless scalar field
which is minimally coupled to the metric. Our implementation will be
coordinate agnostic, and therefore can be used with any of the
curvilinear coordinate systems supported by NRPy+. The resulting code
can be used to study the gravitational collapse of massless scalar
fields, as shown in a [recent publication](https://arxiv.org/abs/2106.06553).
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
