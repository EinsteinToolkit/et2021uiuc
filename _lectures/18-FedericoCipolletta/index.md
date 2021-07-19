---
layout: default
usemathjax: true
title: "Spritz: general relativistic magnetohydrodynamics with neutrinos"
author: Federico Cipolletta
institution: Leonardo HPC LABs - Genova, IT
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
I will present the Spritz GRMHD code aimed at the study of compact binary mergers with finite-temperature equations of state and neutrino physics that is already available for public download. Numerical modeling of NS-NS and NS-BH binary mergers requires a fully general relativistic treatment taking into account accurate magnetic field's evolution and microphysics effects, to extract the most complete physical information from gravitational waves and electromagnetic signals observed. I will summarize the main features of our code, namely: the evolution of a staggered vector potential that automatically satisfies the magnetic field's divergence-free condition; the general treatment for the NS Equation Of State allowing for the use of either analytical or tabulated one; a neutrino leakage scheme that provides a useful tool for the study of the post-merger phase. I will present the tests that we performed, including TOV taking into account electron fraction evolution, temperature effects, neutrino leakage, and magnetic field. I will also show preliminary results obtained by the Spritz code in simulating BNS mergers with tabulated EOS within the collaboration funded by the NASA TCAN 80NSSC18K1488 grant.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

Anything else that should appear after the "front matter" stuff above.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
