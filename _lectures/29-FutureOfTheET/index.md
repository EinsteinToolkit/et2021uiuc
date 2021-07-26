---
layout: default
usemathjax: true
title: "Future of the Einstein Toolkit"
author: Everyone
institution: (Einstein Toolkit)
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
We will discuss future plans for the Einstein Toolkit, both by the core developers and the community as a whole.

This discussion will be open to all, though some discussion starter topics will be presented.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
