s = 0

numbers = []
sums = set()

with open('input') as ifile:
    for line in ifile:
        n = int(line)
        numbers.append(n)
        s += n
        sums.add(s)

print(s)

while True:
    for i in numbers:
        s += i
        if s in sums:
            print(s)
            exit()
        else:
            sums.add(s)
