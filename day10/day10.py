from itertools import count
import fileinput
import re

# parse points into (x, y, vx, vy) tuples
points = [tuple(map(int, re.findall(r'[-\d]+', x))) for x in fileinput.input('input')]


# return (x, y) positions for the stars at time t
def state(points, t):
    return [(x + vx * t, y + vy * t) for x, y, vx, vy in points]


# return the bounding box of the provided points
def bounds(points):
    x0, x1 = min(p[0] for p in points), max(p[0] for p in points)
    y0, y1 = min(p[1] for p in points), max(p[1] for p in points)
    return (x0, y0, x1, y1)


# return the bounding box area of the provided points
def area(points):
    x0, y0, x1, y1 = bounds(points)
    return (x1 - x0 + 1) * (y1 - y0 + 1)


# find the time when bounding area is minimal
# bounding area will decrease, hit a minimum, and then increase
# find when it first increases and return the previous, minimal time value
def min_area_t(points):
    prev = area(points)
    for t in count():
        a = area(state(points, t))
        if a > prev:
            return t - 1
        prev = a


# construct a string to display the stars
def display(points):
    x0, y0, x1, y1 = bounds(points)
    points = set(points)
    rows = []
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            row.append('*' if (x, y) in points else ' ')
        rows.append(''.join(row))
    return '\n'.join(rows)


# find the proper time
t = min_area_t(points)

# part 1: print the stars at time t (no OCR here)
print(display(state(points, t)))

# part 2: print the time
print(t)
