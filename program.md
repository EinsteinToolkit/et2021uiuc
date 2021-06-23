---
layout: default
title: Scientific Program
day1_1:
  title: Welcome/ET status
day1_2:
  title: Binary neutron star ID theory
  tag: AntoniosTsokaros
day1_3:
  title: TBD
  tag: TBD
day1_4:
  title: Maxwell vaccum thorn
  tag: YosefZlochower2
day1_5:
  title: 1D self-force
  tag: PeterDiener
day4_1:
  title: some tutorial

day2_1:
  tag: HelviWitek
day2_2:
  title: LORENE ID I
  tag: MariaBabiuc
day2_3:
  title: TBD
  tag: TBD
day2_4:
  title: Maxwell vaccum thorn, <br>NRPy+ tutorial
  tag:
    - YosefZlochower2
    - LeoWerneck
day2_5:
  title: School V

day3_1:
  title: School I
day3_2:
  title: LORENE ID II
  tag: AtulKedia2
day3_3:
  title: TBD
  tag: TBD
day3_4:
  title: NRPy+ tutorial
  tag: LeoWerneck
day3_5:
  title: Gravitational wave analysis
  tag: DeborahFerguson

day4_1:
  tag: SteveBrandt
day4_2:
  title: Using LORENE data
  tag:
    - BrunoGiocomazzo
    - AtulKedia
day4_3:
  title: Spritz,<br>GRAtenna++
  tag:
    - FedericoCipolletta
    - BorisDaszuta
day4_4:
  title: Con2Prim,<br>SphericalNR
  tag:
    - WolfgangKastaun
    - YosefZlochower2
day4_5:
  title: TBD
  tag: TBD

day5_1:
  tag: DonWillcox
day5_2:
  title: TBD
  tag: TBD
day5_3:
  title: Lighting I (TBD)
  tag: Lighthing1
day5_4:
  title: Lighting II (TBD)
  tag: Lighthing2
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
<th> July 26<sup>th</sup> </th>
<th> July 27<sup>th</sup> </th>
<th> July 28<sup>th</sup> </th>
<th> July 29<sup>th</sup> </th>
<th> July 30<sup>th</sup> </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td markdown="span" rowspan=1><b>{{page.day1_1.title}}{%include title tag=day1_1.tag%}</b></td>
  <td markdown="span"><b>{{page.day1_2.title}}{%include title tag=day1_2.tag%}</b></td>
  <td markdown="span"><b>{{page.day1_3.title}}{%include title tag=day1_3.tag%}</b></td>
  <td markdown="span"><b>{{page.day1_4.title}}{%include title tag=day1_4.tag%}</b></td>
  <td markdown="span" rowspan=2><b>{{page.day1_5.title}}{%include title tag=day1_5.tag%}</b></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td markdown="span" rowspan=2><b>{{page.day2_1.title}}{%include title tag=day2_1.tag%}</b></td>
  <td markdown="span" rowspan=1><b>{{page.day2_2.title}}{%include title tag=day2_2.tag%}</b></td>
  <td markdown="span"><b>{{page.day2_3.title}}{%include title tag=day2_3.tag%}</b></td>
  <td markdown="span"><b>{{page.day2_4.title}}{%include title tag=day2_4.tag%}</b></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td markdown="span"><b>{{page.day3_2.title}}{%include title tag=day3_2.tag%}</b></td>
  <td markdown="span"><b>{{page.day3_3.title}}{%include title tag=day3_3.tag%}</b></td>
  <td markdown="span"><b>{{page.day3_4.title}}{%include title tag=day3_4.tag%}</b></td>
  <td markdown="span"><b>{{page.day3_5.title}}{%include title tag=day3_5.tag%}</b></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td markdown="span"><b>{{page.day4_1.title}}{%include title tag=day4_1.tag%}</b></td>
  <td markdown="span"><b>{{page.day4_2.title}}{%include title tag=day4_2.tag%}</b></td>
  <td markdown="span"><b>{{page.day4_3.title}}{%include title tag=day4_3.tag%}</b></td>
  <td markdown="span"><b>{{page.day4_4.title}}{%include title tag=day4_4.tag%}</b></td>
  <td markdown="span"><b>{{page.day4_5.title}}{%include title tag=day4_5.tag%}</b></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td markdown="span"><b>{{page.day5_1.title}}{%include title tag=day5_1.tag%}</b></td>
  <td markdown="span"><b>{{page.day5_2.title}}{%include title tag=day5_2.tag%}</b></td>
  <td markdown="span"><b>{{page.day5_3.title}}{%include title tag=day5_3.tag%}</b></td>
  <td markdown="span"><b>{{page.day5_4.title}}{%include title tag=day5_4.tag%}</b></td>
  <td markdown="span"><b>{{page.day5_5.title}}{%include title tag=day5_5.tag%}</b></td>
</tr>
</table>
</div>

<div class="col-xs-12">
<h2>Per-day schedules</h2>

All times US Central time.

<div class="row">

<div class="col-sm-6">
<h3>July 26<sup>th</sup>: Numerical Relativity</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th> </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td rowspan=1><div markdown="1"><b>{{page.day1_1.title}}{%include title tag=day1_1.tag%}</b><br>{{page.day1_1.desc}}{%include author tag=day1_1.tag%}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td rowspan=2><div markdown="1">{%include schedule tag=page.day2_1.tag%}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day4_1.tag%}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day5_1.tag%}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>July 27<sup>th</sup>: Initial data</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day1_2.tag%}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day2_2.tag%}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day3_2.tag%}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day4_2.tag%}
</div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day5_2.tag%}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>July 28<sup>th</sup>: Relativistic (magneto)-hydrodynamics</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day1_3.tag%}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day2_3.tag%}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day3_3.tag%}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
 <td><div markdown="1">{%include schedule tag=page.day4_3.tag%}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day5_3.tag%}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>July 29<sup>th</sup>: Thorn writting</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day1_4.tag%}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day2_4.tag%}
  </div></td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day3_4.tag%}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day4_4.tag%}
  </div></td>
</tr>
<tr><td>12:35 AM</td><td>1:20 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day5_4.tag%}
  </div></td>
</tr>
</table>
</div>

<div class="col-sm-6">
<h3>July 30<sup>th</sup>: Data analysis</h3>

<table class="day-schedule">
<tr><th> start </th><th> end </th> <th>  </th>
</tr>
<tr><td>9:00 AM</td><td>9:45 AM</td>
  <td rowspan=2><div markdown="1">{%include schedule tag=page.day1_5.tag%}
  </div></td>
</tr>
<tr><td>9:50 AM</td><td>10:35 AM</td>
</tr>
<tr><td>10:40 AM</td><td>11:25 AM</td>
  <td><div markdown="1">{%include schedule tag=page.day3_5.tag%}
  </div></td>
</tr>
<tr><td>11:25 AM</td><td>11:45 AM</td>
  <td>break</td>
</tr>
<tr><td>11:45 AM</td><td>12:30 PM</td>
  <td><div markdown="1">{%include schedule tag=page.day4_5.tag%}
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

