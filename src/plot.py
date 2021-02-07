import re
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from typing import List

from .classes import Note

year_re = re.compile(r'\d{4}')
note_re = re.compile(r'(\d{2}) ([a-z]{3}) (\d{1,2}) (\d{1,2}):(\d{2}) (\w+)')

colors = {
    'ne': '#00ff00',
    'ib': '#ff0000',
    'null': '#ffffff',
}
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

# def read_input(file: str) -> List[Note]:
#     notes = []
#     year = None
#     for line in open(file).read().split('\n'):
#         if re.match(year_re, line):
#             year = line
#         elif note := re.match(note_re, line):
#             day, month, points, hour, minute, med = note.groups()
#             notes.append(Note(
#                 datetime.datetime(
#                     int(year),
#                     months[month],
#                     int(day),
#                     hour=int(hour),
#                     minute=int(minute)
#                 ),
#                 int(points),
#                 med
#             ))
#     return notes


def gen_plot(notes: List[Note]) -> None:

    x = []
    y = []

    for note in notes:
        x.append(date2num(note.date))
        y.append(note.points)

    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)

    graph = fig.add_subplot(111)
    graph.scatter(x, y, c=[colors.get(note.med) or '#000000'
                           for note in notes], edgecolors='#000000')
    graph.plot(x, y)
    graph.set_xticks(x)
    graph.set_xticklabels([note.date.strftime("%Y-%m-%d") for note in notes])

    plt.xticks(rotation=45)
    plt.savefig('plot.png')

# TODO(#1): discord integration
