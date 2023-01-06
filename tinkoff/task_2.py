def devote(person):
    cut = 0
    while person > 1:
        cut += 1
        person = int(person / 2 + 0.5)
    return cut


if __name__ == '__main__':
    print(devote(int(input())))
