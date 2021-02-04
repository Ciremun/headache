import re
import matplotlib.pyplot as plt
from typing import List, NamedTuple

year_re = re.compile(r'\d{4}')
note_re = re.compile(r'(\d{2}) ([a-z]{3}) (\d{1,2}) (\d{1,2}):(\d{2}) (\w+)')


class Note(NamedTuple):
    day: str
    month: str
    points: str
    hours: str
    minutes: str
    cure: str
    year: str


def read_input(file: str) -> List[str]:
    lines = open(file).read().split('\n')
    notes = []
    year = lines[0]
    for line in lines[1:]:
        if re.match(year_re, line):
            year = line
        elif note := re.match(note_re, line):
            notes.append(Note(
                note.group(1),
                note.group(2),
                note.group(3),
                note.group(4),
                note.group(5),
                note.group(6),
                year
            ))


def main():

    fig, ax = plt.subplots()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    notes = read_input('input.txt')

    plt.scatter(2.0, 1.0)
    plt.savefig('output.png', fmt='png')
    plt.show()


if __name__ == '__main__':
    main()
