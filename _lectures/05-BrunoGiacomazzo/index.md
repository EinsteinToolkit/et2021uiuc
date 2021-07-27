---
layout: default
usemathjax: true
title: "Using LORENE Binary Neutron Star Initial Data"
author: Bruno Giacomazzo
institution: University of Milano-Bicocca
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
In this lecture we will learn how to read binary neutron star initial data generated with LORENE within the Einstein Toolkit. For this lecture we will use a simple piecewise polytropic equation of state (EOS) modeling a cold nuclear EOS. The initial data are contained in ETK_School_2021.tgz. A Jupyter notebook will be used for this tutorial (Giacomazzo_ETK_2021.ipynb). A more complex parameter file that can run on a cluster can be found in BNS_ETK_July_2021_Sly4_lowres.par.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
