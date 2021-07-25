---
layout: default
usemathjax: true
title: "NRPy+ tutorial: Maxwell's equations in flat space"
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
In this tutorial we will provide a thorough introduction of how to
implement tensorial expressions using `NRPy+` and how to generate an
Einstein Toolkit thorn from them. We will focus on the specific case of
Maxwell's equations in flat space using Cartesian coordinates,
showcasing how easy it is to convert symbolic expressions implemented in
Einstein-like notation using the [`SymPy`](https://www.sympy.org/)
package into highly optimized C code that uses both common subexpression
elimination (CSE)  and single instruction, multiple data (SIMD) compiler
intrinsics.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
