still_good = set()
size_range = list(range(1000))
fabric = {}

for i in size_range:
    for j in size_range:
        fabric[(i, j)] = {'id': "", "value": 0}


def fill_fabric(k, start_x, start_y, length_x, length_y):
    for i in range(length_x):
        for j in range(length_y):
            patch = fabric[(i + start_x, j + start_y)]
            patch['value'] += 1
            if patch['value'] > 1:
                still_good.discard(patch['id'])
            patch['id'] = k


def count_fabric():
    count = 0
    for i in size_range:
        for j in size_range:
            patch = fabric[(i, j)]
            if patch['value'] > 1:
                still_good.discard(patch['id'])
                count += 1
    return count


with open('input') as ifile:
    for line in ifile:
        x = line.split()
        key = x[0][1::]
        still_good.add(key)
        fill_fabric(key, int(x[2].split(',')[0]), int(x[2].split(',')[1][:-1]), int(x[3].split('x')[0]),
                    int(x[3].split('x')[1]))
    print(count_fabric())
    print(still_good)
