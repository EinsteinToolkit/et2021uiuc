---
layout: default
usemathjax: true
title: "Introduction to Numerical Relativity"
author: Helvi Witek
institution: The University of Illinois Urbana Champaign
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
slides: IntroNumericalRelativity_Lecture_26July2021-20210726_115857.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
 In this lecture I will give a brief overview on the theoretical foundations of numerical relativity. I will describe the 3+1 decomposition of spacetime and of Einstein's equations. I will touch upon well-posedness of hyberbolic equations, mention well-posed formulations of Einstein's equations and present suitable coordinate choices for stable numerical simulations.

The presentation should be taken as a brief overview and what-is-what of the topic. To study Numerical Relativity in depth, I recommend the excellent textbooks by
[M. Alcubierre 2008](https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/gpjosq/alma99763099712205899),
[Baumgarte & Shapiro 2010](https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/gpjosq/alma99895384312205899),
[Shibata 2015](https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/gpjosq/alma99796368012205899) and
[Baumgarte & Shapiro 2021](https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/gpjosq/alma99954855400705899).
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

During the presentation an number of authors that have worked on well-posedness of numerical relativity were mentioned. This is a partial list of more recent publications relevant for this:

* [Sarbarch & Tiglio](https://inspirehep.net/literature/1095360)
* [Hilditch](https://inspirehep.net/literature/1253348)

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
