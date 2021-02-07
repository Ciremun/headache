import re
from datetime import datetime

import src.db as db

months = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}

lines = """
2020
26 oct 3 12:00 ne
28 oct 1 12:00 null
29 oct 3 12:00 ne
30 oct 3 4:34 ne
31 oct 4 18:14 ne
08 nov 4 23:02 ne
10 nov 4 4:18 ne
13 nov 3 3:30 ne
15 nov 5 6:35 ne
16 nov 2 13:52 ne
20 nov 3 17:02 ne
22 nov 3 16:22 ne
26 nov 3 13:11 ne
28 nov 2 1:06 ne
01 dec 2 17:55 ne
03 dec 3 15:52 ne
05 dec 4 8:51 ne
07 dec 3 1:14 ne
09 dec 3 17:33 ne
13 dec 4 23:24 ne
14 dec 3 17:48 ne
16 dec 3 2:47 ne
21 dec 3 2:43 ne
22 dec 2 0:03 ne
22 dec 3 6:07 ne
24 dec 2 22:56 ib
27 dec 2 13:08 ne
31 dec 3 8:10 ne
2021
01 jan 3 3:31 ne
04 jan 2 9:55 ne
06 jan 2 17:37 ne
12 jan 2 10:30 ne
13 jan 3 17:14 ne
18 jan 2 17:26 ne
19 jan 3 18:52 ne
25 jan 3 15:40 ne
27 jan 2 20:39 ne
28 jan 3 12:19 ne
30 jan 3 20:00 ne
02 feb 2 1:40 ne
06 feb 2 13:11 ne
07 feb 3 13:01 ne
"""

lines = lines.split('\n')

year_re = re.compile(r'\d{4}')
note_re = re.compile(r'(\d{2}) ([a-z]{3}) (\d{1,2}) (\d{1,2}):(\d{2}) (\w+)')

def read_input(lines):
    year = None
    for line in lines:
        if re.match(year_re, line):
            year = line
        elif note := re.match(note_re, line):
            day, month, points, hour, minute, med = note.groups()
            date = datetime(
                    int(year),
                    months[month],
                    int(day),
                    hour=int(hour),
                    minute=int(minute)
                )
            db.add_note(date, int(points), med)

read_input(lines)
