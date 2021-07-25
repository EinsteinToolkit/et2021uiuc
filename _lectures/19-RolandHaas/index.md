---
layout: default
usemathjax: true
title: "Writing an initial data reader thorn"
author: Roland Haas
institution: University of Illinois Urbana-Champaign
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
Good initial data is crucial for numerical relativistic simulations. Whether to
explore the effect of new fields or alternative theories of gravity  or using
initial data generated with a new initial data code, Einstein Toolkit users are
often faced with the task of importing initial data into a simulation.

In this presentation I will cover the basic Cactus design ideas concerned with
initial data, as well as the conventions set forth by the Einstein Toolkit
$$\texttt{ADMBase}$$ and $$\texttt{HydroBase}$$ thorns.

I will demonstrate the concepts using a reader thorn for 2D rotationally
symmetric single neutron stars generated with the
[RNDID](https://bitbucket.org/einsteintoolkit/einsteininitialdata/pull-requests/3/new-initial-data-thorn-for-grhydro/diff)
standalone code.
{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
