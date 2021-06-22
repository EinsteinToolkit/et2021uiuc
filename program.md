---
layout: default
title: Scientific Program
day1_1:
  title: Welcome/ET status
<!--desc: >-
    some long text with a link
    [google](https://google.com)-->
day1_2:
  title: Binary neutron star ID theory
day1_3:
  title: TBD
day1_4:
  title: Maxwell vaccum thorn
day1_5:
  title: 1D self-force
day4_1:
  title: some tutorial
  desc: >-
    Some list:
      * first
      * second
      * third
day2_1:
  title: Numerical relativity
day2_2:
  title: LORENE ID I
day2_3:
  title: TBD
day2_4:
  title: Maxwell vaccum thorn, <br>NRPy+ tutorial
day2_5:
  title: School V

day3_1:
  title: School I
day3_2:
  title: LORENE ID II
day3_3:
  title: TBD
day3_4:
  title: NRPy+ tutorial
day3_5:
  title: Gravitational wave analysis

day4_1:
  title: New user tutorial
day4_2:
  title: Using LORENE data
day4_3:
  title: Spritz,<br>GRAtenna++
day4_4:
  title: Con2Prim,<br>SphericalNR
day4_5:
  title: TBD

day5_1:
  title: AMReX
day5_2:
  title: TBD
day5_3:
  title: Lighting I (TBD)
day5_4:
  title: Lighting II (TBD)
day5_5:
  title: Future of the ET

---

{% include base.html %}


<div class="col-xs-12">
<h1>Program</h1>

<!-- one of https://getbootstrap.com/docs/3.4/components/#alerts -->

</div>

<div class="col-xs-6">
<h2>Time zones</h2>

<div class="tzinfo" markdown="1">

|                 |  start  |  end     |
|-----------------|---------|----------|
| US Central time | 9:00 AM |  1:20 PM |
| US Pacific time | 7:00 AM | 11:20 AM |
| Central EU time | 4:00 PM |  8:20 PM |
| [Other time zones](https://www.timeanddate.com/worldclock/converter.html?iso=20210726T140000&p1=64&p2=51&p3=78&p4=141&p5=176&p6=33&p7=538&p8=240) |  |

</div> <!--tzinfo-->
</div>


<div class="col-xs-12" markdown="1">
## Schedule overview
<div class="alert alert-warning" role="alert">
Tentative, subject to change without notice.
</div>

All times US Central time.


<!-- add schedule entries to the yaml data in the preamble.
     right now you will have to manually add a rowspan attribute and comment
     out some columns for multi-hour entries.
     This templating *could* be all done in Liquid but seems to not be worth
     the effort, though might become interesting if the entries become more
     complex, eg aquire an author and Zoom link entry or so.
-->

<table class="schedule">
<tr><th> start </th><th> end </th>
<th> Day 1 </th>
<th> Day 2 </th>
<th> Day 3 </th>
<th> Day 4 </th>
<th> Day 5 </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td markdown="span" rowspan=1><b>{{page.day1_1.title}}</b></td>
  <td markdown="span"><b>{{page.day1_2.title}}</b></td>
  <td markdown="span"><b>{{page.day1_3.title}}</b></td>
  <td markdown="span"><b>{{page.day1_4.title}}</b></td>
  <td markdown="span" rowspan=2><b>{{page.day1_5.title}}</b></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td markdown="span" rowspan=2><b>{{page.day2_1.title}}</b></td>
  <td markdown="span" rowspan=1><b>{{page.day2_2.title}}</b></td>
  <td markdown="span"><b>{{page.day2_3.title}}</b></td>
  <td markdown="span"><b>{{page.day2_4.title}}</b></td>  
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td markdown="span"><b>{{page.day3_2.title}}</b></td>
  <td markdown="span"><b>{{page.day3_3.title}}</b></td>
  <td markdown="span"><b>{{page.day3_4.title}}</b></td>
  <td markdown="span"><b>{{page.day3_5.title}}</b></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td markdown="span"><b>{{page.day4_1.title}}</b></td>
  <td markdown="span"><b>{{page.day4_2.title}}</b></td>
  <td markdown="span"><b>{{page.day4_3.title}}</b></td>
  <td markdown="span"><b>{{page.day4_4.title}}</b></td>
  <td markdown="span"><b>{{page.day4_5.title}}</b></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td markdown="span"><b>{{page.day5_1.title}}</b></td>
  <td markdown="span"><b>{{page.day5_2.title}}</b></td>
  <td markdown="span"><b>{{page.day5_3.title}}</b></td>
  <td markdown="span"><b>{{page.day5_4.title}}</b></td>
  <td markdown="span"><b>{{page.day5_5.title}}</b></td>
</tr>
</table>
</div>

<div class="col-xs-12">
<h2>Per-day schedules</h2>

All times US Central time.

<div class="row">

<div class="col-sm-6">
<h3>Day 1: Numerical Relativity</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th> </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td rowspan=1><div markdown="1"><b>{{page.day1_1.title}}</b><br>{{page.day1_1.desc}}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td rowspan=2><div markdown="1"><b><a href="{{base}}{{site.lectures[7].url}}">{{site.lectures[7].title}}</a></b><br>{{site.lectures[7].author}}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[10].url}}">{{site.lectures[10].title}}</a></b><br>{{site.lectures[10].author}}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[6].url}}">{{site.lectures[6].title}}</a></b><br>{{site.lectures[6].author}}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>Day 2: Initial data</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[2].url}}">{{site.lectures[2].title}}</a></b><br>{{site.lectures[2].author}}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[8].url}}">{{site.lectures[8].title}}</a></b><br>{{site.lectures[8].author}}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[13].url}}">{{site.lectures[13].title}}</a></b><br>{{site.lectures[13].author}}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[5].url}}">{{site.lectures[5].title}}</a></b><br>{{site.lectures[5].author}}<br><b><a href="{{base}}{{site.lectures[3].url}}">{{site.lectures[3].title}}</a></b><br>{{site.lectures[3].author}}
</div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[19].url}}">{{site.lectures[19].title}}</a></b><br>{{site.lectures[19].author}}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>Day 3: Relativistic (magneto)-hydrodynamics</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[19].url}}">{{site.lectures[19].title}}</a></b><br>{{site.lectures[19].author}}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[19].url}}">{{site.lectures[19].title}}</a></b><br>{{site.lectures[19].author}}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[19].url}}">{{site.lectures[19].title}}</a></b><br>{{site.lectures[19].author}}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
 <td><div markdown="1"><b><a href="{{base}}{{site.lectures[18].url}}">{{site.lectures[18].title}}</a></b><br>{{site.lectures[18].author}}<br><b><a href="{{base}}{{site.lectures[4].url}}">{{site.lectures[4].title}}</a></b><br>{{site.lectures[4].author}} 
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[16].url}}">{{site.lectures[16].title}}</a></b><br>{{site.lectures[16].author}}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>Day 4: Thorn writting</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[12].url}}">{{site.lectures[12].title}}</a></b><br>{{site.lectures[12].author}}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[12].url}}">{{site.lectures[12].title}}</a></b><br>{{site.lectures[12].author}}<br><b><a href="{{base}}{{site.lectures[15].url}}">{{site.lectures[15].title}}</a></b><br>{{site.lectures[15].author}}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[15].url}}">{{site.lectures[15].title}}</a></b><br>{{site.lectures[15].author}}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[11].url}}">{{site.lectures[11].title}}</a></b><br>{{site.lectures[11].author}}<br><b><a href="{{base}}{{site.lectures[14].url}}">{{site.lectures[14].title}}</a></b><br>{{site.lectures[14].author}}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[17].url}}">{{site.lectures[17].title}}</a></b><br>{{site.lectures[17].author}}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>Day 5: Data analysis</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td rowspan=2><div markdown="1"><b><a href="{{base}}{{site.lectures[20].url}}">{{site.lectures[20].title}}</a></b><br>{{site.lectures[20].author}}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[1].url}}">{{site.lectures[1].title}}</a></b><br>{{site.lectures[1].author}}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1"><b><a href="{{base}}{{site.lectures[19].url}}">{{site.lectures[19].title}}</a></b><br>{{site.lectures[19].author}}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1"><b>{{page.day5_5.title}}</b><br>{{page.day5_5.desc}}
  </div></td>
</tr>
</table>
</div>

</div> <!-- row -->
</div> <!-- per-day schedule -->

