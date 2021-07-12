---
layout: default
usemathjax: true
title: New user tutorial
author: Steven Brandt
institution: Louisiana State University
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
recording: https://youtu.be/UXX3qAFQPR4
---
{% include base.html %}

{%-capture abstract-%}
Introduction to the Einstein Toolkit and tutorial for new users.
In this tutorial you will learn how to download and compile the Einstein
Toolkit and a how to run a simple simulation on your local computer.
{%-endcapture-%}

{% include lecture.md abstract=abstract %}

Please refer to the [instructions]({{base}}/instructions.html) page for login instructions into the tutorial server.

Note: the current recording is from the [2020 worshop](https://www.cct.lsu.edu/Einsteintoolkitworkshop) at LSU.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
