---
layout: default
usemathjax: true
title: "GRAthena++"
author: Boris Daszuta
institution: Friedrich-Schiller-Universität Jena
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
recording: https://youtu.be/agzq2qON40o
---
{% include base.html %}

{%-capture abstract-%}
GR-Athena++ is a general-relativistic, high-order, vertex-centered
solver that extends the oct-tree, adaptive mesh refinement
capabilities of the astrophysical (radiation) magnetohydrodynamics
code Athena++. To simulate dynamical spacetimes GR-Athena++ uses the
Z4c evolution scheme of numerical relativity coupled to the moving
puncture gauge. Stable and accurate binary black hole merger
evolutions are demonstrated in convergence testing, cross-code
validation, and verification against state-of-the-art
effective-one-body waveforms. GR-Athena++ leverages the task-based
parallelism paradigm of Athena++ to achieve excellent scalability.
Strong scaling efficiencies above 95% for up to 1.2×1e4 CPUs and
excellent weak scaling up to 1e5 CPUs in a production binary black
hole setup with adaptive mesh refinement are measured. GR-Athena++
thus allows for the robust simulation of compact binary coalescences
and and offers a viable path towards numerical relativity at exascale.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}


[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
