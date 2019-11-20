from collections import defaultdict

x = 0
y = 0

with open('input') as ifile:
    for line in ifile:
        print(line)
        d = defaultdict(int)
        for i in line[0:-1]:
            d[i] = d[i] + 1
        print(d)

        if 2 in d.values():
            x += 1
        if 3 in d.values():
            y += 1

print('x = {}, y = {}'.format(x, y))

print(x * y)
