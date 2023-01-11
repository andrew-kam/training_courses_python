def read_input() -> tuple[int, list[int]]:
    input_len = int(input().strip())
    input_students = list(map(int, input().strip().split()))
    return input_len, input_students


def get_answer(students: list[int]) -> list[int]:
    list_even, list_odd = [], []
    for i in range(len(students)):
        if i % 2 == 0 and students[i] % 2 == 0:
            list_even.append(i + 1)
        if i % 2 == 1 and students[i] % 2 == 1:
            list_odd.append(i + 1)

    if len(list_odd) == len(list_even) == 0\
            and len(students) >= 3:
        return [1, 3]
    elif len(list_odd) == len(list_even) == 1:
        return [list_odd[0], list_even[0]]\
            if list_odd[0] < list_even[0]\
            else [list_even[0], list_odd[0]]
    else:
        return [-1, -1]


def main():
    len_student, students = read_input()
    print(*get_answer(students))


if __name__ == '__main__':
    main()
