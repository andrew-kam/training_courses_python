class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError


l = PositiveList()
for i in range(5):
    l.append(int(input()))
print(l)
