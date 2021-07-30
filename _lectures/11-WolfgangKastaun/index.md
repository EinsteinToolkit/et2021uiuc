---
layout: default
usemathjax: true
title: "The joy of primitive variable recovery in relativistic magnetohydrodynamics"
author: Wolfgang Kastaun
institution: Max Planck Institute for Gravitational Physics
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
recording: https://youtu.be/6n4b6SMEUZQ
---
{% include base.html %}

{%-capture abstract-%}
Modern evolution codes for general relativistic magnetohydrodynamic are all based on evolution equations in form of 
a conservation law. The evolved variables depend on the fundamental (primitive) variables such as density and velocity 
in a nonlinear fashion that has proven difficult to invert robustly. One problem is the need to cover wastly different 
regimes from magnetically dominated to non-magnetized, and from the Newtonian limit to highly relativistic cases.
Another problem is the need to handle physically invalid combinations of the evolved variables caused by evolution 
errors. Failure of the primitive variable recovery has been a major and persistent source of problems for such 
simulations. I will describe the problem and summarize various approaches, with focus on a new public library I 
recently made public.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
