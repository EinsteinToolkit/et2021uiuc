---
layout: default
usemathjax: true
title: "SphericalNR"
author: Vassilios Mewes
institution: ORNL
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
$${\tt SphericalNR}$$ is a new dynamical spacetime and general relativistic 
MHD evolution framework in spherical coordinates for the $${\tt Einstein Toolkit}$$. 
This talk will present the framework, highlighting algorithmic developments to solve
hyperbolic PDEs in spherical coordinates within the Cartesian code base of the 
$${\tt Einstein Toolkit}$$ as well as recent developments, including higher order 
reconstruction methods and an improved atmosphere treatment. 

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
