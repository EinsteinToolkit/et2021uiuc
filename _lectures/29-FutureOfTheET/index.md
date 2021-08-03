---
layout: default
usemathjax: true
title: "Future of the Einstein Toolkit"
author: Everyone
institution: Einstein Toolkit
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

## Minutes

### New physics in the ET - what can you almost but not quite do in the ET and have code of your own that does let you do it?
* Roland mentioned cosmology as a new area of simulations that is now being explored with the ET
* Helvi Witek mentioned the FRW code Hayley Mcpherison reported on, the Sprittz code, the con2prim library Wolfgang Kastaun reported on
* There was a request about what the steps to contribute code to the Einstein Toolkit are
  * Roland Haas showed "How to contribute" page of the toolkit website
  * Authors should start be contacting maintainers
  * Plan on 3-4 months (one release cycle) to add any code due to time required to find volunteers and volunteers to work on the review
  * Contributed code comes with (perpetual) authorship of the ET
  * Wolfgang asked about what kind of dependencies contributed code can depend on, giving the example of the Meson build system used by RePriMand
    * Roland suggested to not require software that is not typically found on public clusters and cannot be provided by ExternalLibraries
    * These requirements are a bit stricter for Cactus thorns that are enabled by default, but are less strict for standalone code, for example the self-force 1D code
    * Erik Schnetter pointed out the toolkit contains more than just Cactus thor
      * Need to provide well written build instructions similar to the requirements by the journal of open source software
      * Self-tests would then run in containers
    * Erik observed that contributing to the toolkit is seem as a difficult and somewhat opaque procedure, which should not be the case and may limit contributions
    * Currently not all code in the ET has automated self-tests, mostly the thorns only but not eg Self-Force 1D or (most of) the scripts

### Expanding the user base - The Einstein Toolkit is for its users and y its user. How to engage with users and encourage active contribution.
* Would want to make it easier for user to interact with the ET, in particular via the  Thursday ET calls
* Would also want to provide more way to learn about the ET
  * Idea to provide tutorials similar to the ones in the school along with the existing series of Einstein Toolkit seminars
  * Surveyed interest by the audience if they would be interested in listening and als presenting in such a tutorial
  * Wolfgang would be interested in presenting in more detail on the problems concerning con2prim
  * Alex Van-Vinuale would be interested in having more regular classes on visualization and postprocessing Einstein Toolkit data
    * Wolfgang mentioned that PostCactus will receive a major update in 2 months or so and he would be happy to present
  * Steve Brandt asks for copies of any Jupyter notebooks used so that he can include them in the tutorial server so that they are available to any user using the tutorial server
  * Interest exists in short tutorials on how to write parameter files or how to set up the ET on a Linux cluster
    * There is also interest in the presenting one's own experience on how these tutorials actually worked for you
  * It was mentioned that a longer series on NR and GR would also be interesting.
    * Helvi and Bruno Giacommazzo are or will be teaching classes like this, that are being recorded already. Bruno suggested to add lecture notes and book links to the ET page, beyond the existing links on the wiki https://docs.einsteintoolkit.org/et-docs/Main_Page#Documentation some standard literature is listed on the presentaion page for Helvi's lecture on Monday https://einsteintoolkit.github.io/et2021uiuc/lectures/07-HelviWitek/index.html . Would have to check with their respective home institutions if that is possible.
  * Helvi shared the mailing list address users@einsteintoolkit.org which one can sing up for at http://lists.einsteintoolkit.org/mailman/listinfo/users 
* Wolfgang suggests an API to handle Einstein Toolkit output data for postprocessing, including outputting more metadata
  * Erik suggests that outputting this information from the point of view of the driver is not hard and should be done
  * Steve Brandt suggested creating a ticket for this to keep track of progress
* Vassilios Mewes asked about TRIGGER clauses for ANALYSIS bin routines and somewhat non-reproducible behaviour he is observing
  * Erik suggest avoiding TRIGGER clauses
  * Steve Brandt's work on correctness checking ("presync") will help avoid many of these issues, as long as all scheduled routines properly declare "READS" and "WRITES" clauses in their schedule.ccl .

### CarpetX - hydrodynamics -- CarpetX is the designated driver for the future ET, designed for faster / bter radiation - magneto - hydrodynamics.
* Roland asked about the difficulties seen in adapting to CarpetX
* Wolfgang mentions not being sure how ot visualize CarpetX output
  * Erik reports on CarpetX's Silo output capabilities
* Ian Hawke observes that CarpetX seems to move towards no subcycling in time and more smaller gird patches
    * Asks about whether there has been a any study on how this affects accuracy, efficiency, and effects from the increased number of mesh refinement boundaries. Is there a good mesh refinement criterion yet?
* Currently none of tis has been fully checked
* Ian pointed out that in the early days when local mesh refinement was used it was found that results tended to be bad unless the GW fron was well resolved but this issue mostly showed up in global quantities and not in easily locally measurable quantities
* Erik pointed out that GRAthena++ also seems to use box in box refinement for BH even in an octant based tree
  * Vassilios mentions that these issue have existed in GRAthena++ for a while
* Ian cautioned about dispersion error due to larger number of mesh refinement boundaries and that the required dissipation to handle this may destroy much fo the efficiency gain
* CarpetX is currently barely able ot run interesting simulations and having it be used will uncover which parts are missing
* Yosef Zlochower confirms that issue about local error estimates are also an issue for Dendro, so that they obtain well controlled GW error
  * To remain efficient one needs to avoid resolving the junk radiation
* For Bruno the major driver for CarpetX is its GPU support, given that most large clusters employ GPUs now
  * Vassili mentioned that ET is very nice on CPU clusters, asks how realistic it is to expect that CarpetX would provide and equally easy to use interface to heterogeneous hardware
  * Erik considered this realistic, not everything that Carpet supports will be supported, but most interesting parts. Currently there are no scalability tests for CarpetX yet compared to Carpet, so there is a danger that some re-design of the code is required
  * Wolgang mentions that some problems are better suited for GPUs than others, eg con2prim is hard to do. Ian reported that a student of his ported a special relativistic HD code to GPUs and saw similar speedups than what is typically seen for non-relativistic HD code where there is no con2prim
  * Roland mostly worries about the data movement required if not everything runs on CPUs which may require porting a larger amount of code to GPUs
  * Ian brought up the issue about retrials of steps similar to an IMEX or predictor-corrector code which is easy to add to a pure CPU code like MoL but might be harder in a more tightly coupled code like CarpetX. Erik thinks this may be possibly in a similar way
  * In summary GPU support is one of the big draws for CarpetX even at the cost that not all existing code will be portable to it
* Wolfgang suggested adding more functionality to the 'reduction' interface for example 'histograms'. Will create a enhancement ticket for this, Erik may have time to look into this.
* Helvi would be interested in porting some of the beyond-GR thorns to CarpetX
  * Erik would be interested, suggests that best is if there are groups interested in it so that Helvi spends time efficiently
  * Roland outlines his view that testing with many codes early will allow the driver  and framework to be constructed to support a wide array of applications while once the drive has been around for a number of yrears its interface will fossilize or freeze and will be harder to change
  * CarpetX's capabilities should be driven by science code needs
* Vassilios would be interested in a finite difference MHD code for CarpetX

### Other cool applications for the ET or areas where it is falling behind
* Steve mentioned Zacharia Etienne's Black-holes-at-home project, which computes BBH templates on people's home computers
* Wolfgang and Steve mentions the difficulty of interacting with the build system. Two issues are mentioned:
  * Code generation during CST stage based on information in ccl files
  * Non-obvious use of GNU make in some places, difficult to trace data dependencies and interactions
* Progress will be limited by available person-power, and testing on all supported clusters
  * Erik mentions that there is a UK call for modernizing existing software that one may get involved with


[Edit on GitHub](https://github.com/EinsteinToolkit/et2021uiuc/edit/master/{{page.path}})
</div>
