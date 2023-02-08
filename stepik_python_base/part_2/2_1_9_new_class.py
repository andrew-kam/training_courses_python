class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError


def create_positive_list(i):
    list_positive = PositiveList()
    for _ in range(i):
        list_positive.append(int(input()))
    print(list_positive)


if __name__ == '__main__':
    n = 10
    create_positive_list(n)

# https://stepik.org/lesson/24463/step/9?unit=6771
