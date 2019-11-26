import re

count = {}


def do_react(a, b):
    return a.upper() == b.upper() and a != b


def remove_reactive(a, replace):
    pattern = re.compile(a, re.IGNORECASE)
    return pattern.sub("", replace)


def reduce(to_be_reduced):
    i = 0
    while i < len(to_be_reduced) - 1:
        if do_react(to_be_reduced[i], to_be_reduced[i + 1]):
            to_be_reduced = to_be_reduced.replace(to_be_reduced[i] + to_be_reduced[i + 1], '')
            if i > 1:
                i -= 1
        else:
            i += 1
    return to_be_reduced


with open('input') as ifile:
    for line in ifile:
        line = line[:-1]
        min_len = len(line)
        for j in range(len(line)):
            if count.get(line[j]) is None:
                reduced = reduce(remove_reactive(line[j], line))
                if len(reduced) < min_len:
                    min_len = len(reduced)
                count[line[j]] = len(reduced)
        print(min_len)
