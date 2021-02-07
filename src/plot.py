import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from typing import List

from .classes import Note

colors = {
    'ne': '#00ff00',
    'ib': '#ff0000',
    'null': '#ffffff',
}


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