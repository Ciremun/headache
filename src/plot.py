import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from typing import List

import src.db as db
from .classes import Note


def gen_plot(notes: List[Note]) -> None:

    x = []
    y = []
    points = {}
    colors = {med: color for color, med in db.get_meds()}

    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)

    graph = fig.add_subplot(111)

    for note in notes:
        x_s = date2num(note.date)
        y_s = note.points
        x.append(x_s)
        y.append(y_s)
        color = colors.get(note.med) or '#000000'
        point = graph.scatter(x_s, y_s, c=color, edgecolors='#000000')
        if points.get(note.med) is None:
            points[note.med] = point

    plt.legend(list(points.values()), list(points.keys()))

    graph.plot(x, y)
    graph.set_xticks(x)
    graph.set_xticklabels([note.date.strftime("%Y-%m-%d") for note in notes])

    plt.xticks(rotation=45)
    plt.savefig('flask/plot.png')
