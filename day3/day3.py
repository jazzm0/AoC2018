class Cell:
    id: str
    value: int

    def __init__(self):
        self.value = 0
        self.id = ''


still_good = set()
size = 1000
fabric = [[Cell() for i in range(size)] for j in range(size)]


def fill_fabric(k, start_x, start_y, length_x, length_y):
    for i in range(length_x):
        for j in range(length_y):
            fabric[i + start_x][j + start_y].value += 1

            if fabric[i + start_x][j + start_y].value > 1:
                still_good.discard(fabric[i + start_x][j + start_y].id)

            fabric[i + start_x][j + start_y].id = k


def count_fabric():
    count = 0
    for i in range(size):
        for j in range(size):
            if fabric[i][j].value > 1:
                still_good.discard(fabric[i][j].id)
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
