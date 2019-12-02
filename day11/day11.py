serial = 8444
table = {}


def calc_power(x, y, serial):
    if not table.get((x, y)) is None:
        return table[(x, y)]
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    r = (power_level - (power_level // 1000) * 1000) // 100 - 5
    table[(x, y)] = r
    return r


def sum_nxn(x, y, n):
    part = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            part += calc_power(i, j, serial)
    return part


m = 0
maxX, maxY = 0, 0
size = 0
for i in range(1, 298):
    for j in range(1, 298):
        for k in range(1, 20):
            s = sum_nxn(i, j, k)
            if s > m:
                m = s
                maxX = i
                maxY = j
                size = k

print(maxX, maxY, size)
