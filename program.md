---
layout: default
title: Scientific Program

# day schedules:
# a list of tags for each lecture
# a brak can be given as "breakX"
# 5 minutes breaks are added at the end of lectures hwere needed
# if no duration given it is assumed to be 45min for lectures and 20min for a break

start: "8:25"
end: "13:20"
granularity: 300

day1:
  - Welcome:
      duration: 15
  - HelviWitek:
      duration: 60
  - HelviWitek:
      duration: 60
  - break
  - SteveBrandt
  - DonWillcox
  - ShortLightning1:
      duration: 30

day2:
  - JoshuaFaber:
      duration: 95
  - AtulKedia2
  - break
  - BrunoGiacomazzo
  - GabrieleBozzola:
      duration: 30
  - ErikSchnetter

day3:
  - VassiliosMewes:
      duration: 60
  - VassiliosMewes:
      duration: 65
  - break
  - FedericoCipolletta
  - BorisDaszuta
  - Lightning1

day4:
  - SamTootle:
      duration: 30
  - YosefZlochower
  - LeoWerneck
  - break
  - TBD:
      duration: 40
  - WolfgangKastaun:
      duration: 20
  - YosefZlochower2:
      duration: 25
  - Lightning2

day5:
  - ShortLightning2:
      duration: 30
  - PeterDiener
  - TBD
  - break
  - DeborahFerguson
  - BarryWardell
  - FutureOfTheET

---

{% include base.html %}


<div class="col-xs-12">
<h1>Program</h1>

<!-- one of https://getbootstrap.com/docs/3.4/components/#alerts -->

</div>

<div class="col-xs-6">
<h2>Time zones</h2>

<div class="tzinfo" markdown="1">

|                 |  start                            |  end                            |
|-----------------|-----------------------------------|---------------------------------|
| US Central time | {{page.start | date: "%I:%M %p"}} | {{page.end | date: "%I:%M %p"}} |
| US Pacific time | {{page.start | date: "%s" | minus: 7200 | date: "%I:%M %p"}} | {{page.end | date: "%s" | minus: 7200 | date: "%I:%M %p"}} |
| Central EU time | {{page.start | date: "%s" | plus: 25200 | date: "%I:%M %p"}} | {{page.end | date: "%s" | plus: 25200 | date: "%I:%M %p"}} |
| [Other time zones](https://www.timeanddate.com/worldclock/converter.html?iso=20210726T140000&p1=64&p2=51&p3=78&p4=141&p5=176&p6=33&p7=538&p8=240) |  |

</div> <!--tzinfo-->
</div>


<div class="col-xs-12" markdown="1">
## Schedule overview
<div class="alert alert-warning" role="alert">
Tentative, subject to change without notice.
</div>

All times US Central time.

{% assign starttime = page.start | date: "%s" | plus: 0-%}
{%-assign endtime = page.end | date: "%s" | plus: 0-%}
{%-assign duration = endtime | minus: starttime | plus: page.granularity | minus: 1-%}
{%-assign maxrow = duration | divided_by: page.granularity | minus: 1%}

<table class="schedule">
<tr><th> time </th>
<th> July 26<sup>th</sup> </th>
<th> July 27<sup>th</sup> </th>
<th> July 28<sup>th</sup> </th>
<th> July 29<sup>th</sup> </th>
<th> July 30<sup>th</sup> </th>
</tr>
<tr><td>7:55 AM</td>
  <td>setup help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
</tr>
{%-for row in (0..maxrow)-%}
  {%-assign time = row | times: page.granularity | plus: starttime | date: "%I:%M %p"-%}
  {%-assign half_hour = row | modulo: "6"-%}
  {%-assign timerows = maxrow | minus: row | plus: 1-%}
  {%-comment-%} grow final time block to exactly end at the final time {%-endcomment-%}
  {%-if timerows > 6-%}
    {%-assign timerows = 6-%}
  {%-endif-%}
  <tr>
  {%-if half_hour == 0 and timerows >= 0-%}
  <td rowspan={{timerows}} {% cycle "time": "style='background: #EEE'", ""-%}> {{time}}</td>
  {%-endif-%}
  {% include intersect day=page.day1 column="day1" row=row-%}
  {%-include intersect day=page.day2 column="day2" row=row-%}
  {%-include intersect day=page.day3 column="day3" row=row-%}
  {%-include intersect day=page.day4 column="day4" row=row-%}
  {%-include intersect day=page.day5 column="day5" row=row %}
  </tr>
{%-endfor-%}
<tr><td>1:20 PM</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
  <td>tutorial help</td>
</tr>
</table>

</div>

<div class="col-xs-12">
<h2>Per-day schedules</h2>

All times US Central time.

<div class="row fix">

<div class="col-sm-6">
<h3>July 26<sup>th</sup>: Numerical Relativity</h3>

{% include day_schedule_table.html day=page.day1 %}

</div>

<div class="col-sm-6">
<h3>July 27<sup>th</sup>: Initial data</h3>

{% include day_schedule_table.html day=page.day2 %}

</div>

<div class="col-sm-6">
<h3>July 28<sup>th</sup>: Relativistic (magneto)-hydrodynamics</h3>

{% include day_schedule_table.html day=page.day3 %}

</div>

<div class="col-sm-6">
<h3>July 29<sup>th</sup>: Thorn writting</h3>

{% include day_schedule_table.html day=page.day4 %}

</div>

<div class="col-sm-6">
<h3>July 30<sup>th</sup>: Data analysis</h3>

{% include day_schedule_table.html day=page.day5 %}

</div>

</div> <!-- row -->
</div> <!-- per-day schedule -->

