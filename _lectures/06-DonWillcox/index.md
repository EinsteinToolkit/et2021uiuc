---
layout: default
usemathjax: true
title: "AMReX"
author: Donald Willcox
institution: Lawrence Berkeley National Laboratory
# updload your slides as slides.pdf
# upload your recorded talk as recording.mp4
# all other files in this directory will show up as "additional files"
# alternatively you can override by uncommenting and giving an explict URL:
#slides: myslides.pdf
#recording: https://youtu.be/GYJzhxWWBB8
---
{% include base.html %}

{%-capture abstract-%}
AMReX is a software framework containing all the functionality to write
massively parallel, block-structured adaptive mesh refinement (AMR)
applications.

Key features of AMReX include:
* Primarily C++ with Fortran interfaces available
* Support for 1D, 2D and 3D
* Support for cell-centered, face-centered, edge-centered, and nodal data
* Support for particles and particle-mesh operations
* Support for embedded boundary (cut cell) representations of complex geometries
* Support for hyperbolic, parabolic, and elliptic solves on hierarchical adaptive grid structure
* Optional subcycling in time for time-dependent PDEs
* Hybrid parallelization strategy based on MPI+X, where X is OpenMP for multicore architectures, and primarily CUDA for architectures including NVIDIA GPUs and HIP for architectures including AMD GPUs
* Highly efficient parallel I/O, including native and hdf5 format
* Plotfile format supported by AmrVis, VisIt, ParaView, and yt.

{%-endcapture-%}

<div class="col-xs-12" markdown="1">
{% include lecture.md abstract=abstract %}

[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
