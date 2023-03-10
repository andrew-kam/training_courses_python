class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError


def create_positive_list():
    n = int(input())
    list_positive = PositiveList()
    for _ in range(n):
        list_positive.append(int(input()))
    print(list_positive)


def main():
    create_positive_list()


if __name__ == '__main__':
    main()


# https://stepik.org/lesson/24463/step/9?unit=6771
