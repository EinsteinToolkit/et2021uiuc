---
layout: default
usemathjax: true
title: kuibit: Analyzing Einstein Toolkit simulations with Python
author: Gabriele Bozzola
institution: University of Arizona
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}

[kuibit](https://sbozzolo.github.io/kuibit/) is a free and open-source Python library to analyze and visualize Einstein Toolkit simulations. By taking care of the low levels details (e.g., reading files, parsing the content, ...) and providing intuitive abstractions, the package allows users to focus on their scientific goals. In this talk, I am going to give a broad overview of the project. In particular, I will go over some of the most important features and discuss how to get started with using the library.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

