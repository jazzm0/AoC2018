from collections import defaultdict

x = 0
y = 0

str_list = []


def one_apart(a, b):
    length = min(len(a), len(b))
    k, diff, result = 0, 0, ''
    while k < length:
        if a[k] != b[k]:
            diff += 1
        else:
            result = result + a[k]
        k += 1
        if diff > 1:
            return

    print(result)


with open('input') as ifile:
    for line in ifile:
        d = defaultdict(int)
        for i in line[0:-1]:
            d[i] = d[i] + 1

        if 2 in d.values():
            x += 1
        if 3 in d.values():
            y += 1
        for j in str_list:
            one_apart(j, line)
        str_list.append(line)

print('x = {}, y = {}'.format(x, y))

print(x * y)
