---
layout: default
usemathjax: true
title: "Welcome"
author: Roland Haas
institution: The University of Illinois Urbana Champaign
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
The Einstein Toolkit is a community-driven software platform of core
computational tools to advance and support research in relativistic
astrophysics and gravitational physics.

I report on current research acitivities in the current "Lorentz" release of
the Einstein Tookkit, activity in the ticketing system and mailing and future
development plans.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
