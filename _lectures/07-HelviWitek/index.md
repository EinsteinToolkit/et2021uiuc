---
layout: default
usemathjax: true
title: Numerical relativity
author: Helvi Witek
institution: The University of Illinois Urbana Champaign
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
The abstract describing the lecture. In this lecture we will learn about

* ham
* spam
* eggs

and use $$\LaTeX$$ to display

$$
\begin{equation}
E = m c^2
\end{equation}
$$
{%-endcapture-%}

{% include lecture.md abstract=abstract %}

Anything else that should appear after the "front matter" stuff above.

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
