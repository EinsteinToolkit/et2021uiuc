---
layout: default
usemathjax: true
title: CarpetX
author: Erik Schnetter
institution: Perimeter Institute
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
CarpetX, a new driver for the Einstein Toolkit based on AMReX, is now available for testing. A driver in the Einstein Toolkit is responsible for basic computational algorithms such as adaptive mesh refinement, parallelism, inter-processes communication, or GPU offloading. Thorns can then implement the physics bits and discretization methods, relying on the driver to stitch everything together into a single application. CarpetX offers a range of new features for the Einstein Toolkit that are interesting for hydrodynamics or magnetic fields (staggered grids, refluxing), improved performance (multi-threading, GPUs, scalability, I/O), and additional safety features that prevent or catch programming errors (uninitialized grid points, inconsistent definitions). I will describe these new features and how to use them.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}


<!--[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})-->
</div>
