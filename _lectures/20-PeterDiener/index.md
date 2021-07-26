---
layout: default
usemathjax: true
title: "Time domain self-force with discontinuous Galerkin code: SelfForce1D"
author: Peter Diener
institution: Louisiana State University 
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}

I will describe a time domain code aimed at performing evolutions of
Extreme Mass Ratio Inspirals (EMRIs), i.e. a small compact object (BH or NS)
spiraling into a super massive black hole due to the emission of gravitational
waves. I will give some background to the physical problem and describe some
of the design choices. I will finally demonstrate some of the capabilities
and discuss the outlook for further developments.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

Anything else that should appear after the "front matter" stuff above.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
