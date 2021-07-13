---
layout: default
usemathjax: true
title: Introduction to the Einstein Toolkit
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
This course covers the basics of the Einstein Toolkit:

  1. A brief history;
  2. what the Einstein Toolkit is and can do;
  3. How to install the ET (including prerequisites)
  4. How to run the ET and create a rudimentary plot of some of the data generated.

All of the above steps are carried out within a
Jupyter notebook. This means that there are no hardware
requirements for your computer.

Familiarity with the linux command line is required,
and some minimal knowledge of Python is helpful.

Note that this course replicates the material available in
the online tutorial.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

Please refer to the [instructions]({{base}}/instructions.html) page for login instructions into the tutorial server.

Note: the current recording is from the [2020 worshop](https://www.cct.lsu.edu/Einsteintoolkitworkshop) at LSU.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
