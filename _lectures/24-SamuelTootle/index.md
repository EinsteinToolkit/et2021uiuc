---
layout: default
usemathjax: true
title: "Introduction to FUKA ID"
author: Samuel Tootle
institution: Goethe Universitaet
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
This talk will provide an overview of the implementation and capabilities of the FUKA initial data solvers as well as provide a brief introduction to help users to get started using the solvers.  FUKA is a new public code focused on the generation of constraint satisfying initial data of unequal-mass, spinning compact-object binaries with the added ability to perform eccentricity reduction using Post-Newtonian estimates or iterative reduction techniques.
[https://kadath.obspm.fr/fuka/](https://kadath.obspm.fr/fuka/)
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
