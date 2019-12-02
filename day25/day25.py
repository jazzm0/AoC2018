coordinates = []


def distance(a, b):
    d = 0
    for i in range(4):
        d += abs(a[i] - b[i])
    return d <= 3


def can_merge(a, b):
    for i in a:
        for j in b:
            if distance(i, j):
                return True
    return False


with open('input') as ifile:
    for line in ifile:
        line = line[:-1]
        s = [int(i) for i in line.split(",")]
        point = set()
        point.add((s[0], s[1], s[2], s[3]))
        coordinates.append(point)

has_changed = True
while has_changed:
    has_changed = False
    length = len(coordinates)
    x = 0
    while x < length:
        y = x + 1
        while y < length:
            if can_merge(coordinates[x], coordinates[y]) and coordinates[x] != coordinates[y]:
                for z in coordinates[y]:
                    coordinates[x].add(z)
                coordinates.remove(coordinates[y])
                length = len(coordinates)
                has_changed = True
            else:
                y += 1
        x += 1
print(len(coordinates))
