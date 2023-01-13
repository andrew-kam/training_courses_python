def read_input() -> tuple[int, list[int]]:
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def convert(list_items: list[int]) -> list[int]:
    return [item - 1 for item in list_items]


def checker(students: list[int]) -> bool:
    track = {0}
    ai = students[0]
    while ai not in track:
        track.add(ai)
        ai = students[ai]
    if ai == 0:
        return len(track) == len(students)
    return False


def swap(students: list[int], x: int, y: int) -> list[int]:
    redirected_students = students.copy()
    redirected_students[x] = y
    return redirected_students


def get_answer(students: list[int]) -> tuple[int, int]:
    students = convert(students)
    students_len = len(students)

    if len(set(students)) == students_len - 1:

        stack = [0 for _ in range(students_len)]
        for student in students:
            stack[student] += 1

        double_gifted = stack.index(2)
        no_gifted = stack.index(0)

        indexes_double = [i for i in range(students_len)
                          if students[i] == double_gifted]
        if checker(swap(students, indexes_double[0], no_gifted)):
            return indexes_double[0] + 1, no_gifted + 1
        elif checker(swap(students, indexes_double[1], no_gifted)):
            return indexes_double[1] + 1, no_gifted + 1

    return -1, -1


def main():
    students_len, students = read_input()
    print(*get_answer(students))


if __name__ == '__main__':
    main()

    assert not checker(convert([1, 3, 1]))
    assert checker(convert([2, 3, 1]))
    assert not checker(convert([2, 1, 4, 5, 3]))
    assert not checker(convert([2, 3, 2]))
    assert checker(convert([2, 3, 4, 5, 1]))

    assert get_answer([1, 2, 3]) == (-1, -1)
    assert get_answer([1, 3, 1]) == (1, 2)
    assert get_answer([2, 1, 2, 3, 4]) == (1, 5)
    assert get_answer([2, 1, 4, 5, 3]) == (-1, -1)
    assert get_answer([2, 2]) == (2, 1)
    assert get_answer([2, 3, 1]) == (-1, -1)

    assert swap([1, 1], 1, 0) == [1, 0]
    assert swap([1, 0, 1, 2, 3], 0, 4) == [4, 0, 1, 2, 3]

    assert swap([2, 2], 1, 1) == [2, 1]
    assert swap([2, 1, 2, 3, 4], 0, 5) == [5, 1, 2, 3, 4]
