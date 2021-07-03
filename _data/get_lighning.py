#!/usr/bin/env python3

import requests
import csv
import io
import sys
import os
import re

# this pulls the same CSV file that populates the participants table in
# programl.html
resp = requests.get("https://script.google.com/macros/s/AKfycbzaO60lL2WDcgor8HZ_vnwc1AbDs0ezXt4Xg-tEaPHcUVBS2zqTjUDnUDYNwzq_kfWD/exec")

# append a "tag" to each contributed talk and output only tag, name,
# institution, title, abstract
participants = csv.reader(io.StringIO(resp.text, newline='\r\n'))
medir = os.path.dirname(os.path.abspath(__file__))

rows = []
first = True
for participant in participants:
    if first:
        first = False
        continue

    approved = participant[2] == "TRUE" and participant[3] == "TRUE"
    name = participant[4]
    institution = participant[5]
    title = participant[6]
    abstract = participant[7]
    slideurl = participant[8].split(',')[-1]

    tag = name.replace(' ', '').replace('-', '')

    if approved:
        rows.append([tag, name, institution, title, abstract])
        if slideurl:
            m = re.match(r"https://drive.google.com/open[?]id=(.*)", slideurl)
            id = m.group(1)
            directslideurl = "https://docs.google.com/uc?export=download&id=" + id
            slide = requests.get(directslideurl)
            slidefn = os.path.join(medir, "..", "lightning", tag+".pdf")
            with open(slidefn, "wb") as slidefh:
                slidefh.write(slide.content)

rows.sort(key = lambda row: row[1])
rows = [["tag", "name", "institution", "title", "abstract"]] + rows;

with open(os.path.join(medir, "lightning.csv"), "w", newline='\n') as fh:
    lightning = csv.writer(fh)
    lightning.writerows(rows)

