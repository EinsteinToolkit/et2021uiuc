---
layout: default
usemathjax: true
title: "Introduction to GRMHD"
author: Vassilios Mewes 
institution: ORNL
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
slides: slides.pdf 
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
This lecture will introduce the equations of general relativistic magnetohydrodynamics in a 3+1 split and how to solve them numerically in a finite volume scheme. The second part will connect the theory with a code implementation, highlighting the necessary building blocks of GRMHD and their scheduling in the $${\tt GRHydro}$$ thorn. 


{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}



[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
