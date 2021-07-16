---
layout: default
usemathjax: true
title: Binary neutron star ID theory	
author: Joshua Faber
institution: Rochester Institute of Technology
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
In this talk, I will cover many of the theoretical aspects of generating
binary neutron star initial data.  This will include a discussion of the
different formalisms used, as well as the different numerical
approaches. Comparisons to black holes will include a discussion of why
neutron stars often require different techniques due to both their
hydrodynamic properties as well as the existence of a stellar surface,
the latter of which presents a surprising challenge in developing
highly accurate numerical schemes.  The talk will also discuss the
typical physical assumptions made about NS masses, spins, and equations
of state (the relationship between pressure and density inside the
neutron star), as well as the physical effects that have proven to be
more difficult to model self-consistently, in particular the inclusion
of magnetic fields.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}


<!--[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})-->
</div>
