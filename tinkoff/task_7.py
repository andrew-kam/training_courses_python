def read_input() -> tuple[int, list[int]]:
    len_student = int(input().strip())
    students = list(map(int, input().strip().split()))
    return len_student, students


def checker(students: list[int]) -> bool:
    base_list = [x + 1 for x in range(len(students))]
    ai = students[0]
    while len(base_list) > 0:
        if ai in base_list:
            base_list.remove(ai)
            ai = students[ai - 1]
        else:
            return False
    return True


def double(students: list[int]):
    list_double = []
    list_lack = []
    indexes_double = []
    base_list = [x + 1 for x in range(len(students))]

    for item in base_list:
        if item not in students:
            list_lack.append(item)
        if students.count(item) == 2:
            list_double.append(item)
    if len(list_double) == 1:
        indexes_double = [i for i in range(len(students))
                          if students[i] == list_double[0]]
    return list_double, list_lack, indexes_double


def swap(index, lack, students):
    students_new = students[:]
    students_new[index] = lack
    return students_new


def main():
    len_student, students = read_input()

    list_double, list_lack, indexes_double = double(students)

    if len(indexes_double) == 2 and checker(swap(indexes_double[0], list_lack[0], students)):
        print(indexes_double[0] + 1, list_lack[0])
    elif len(indexes_double) == 2 and checker(swap(indexes_double[1], list_lack[0], students)):
        print(indexes_double[1] + 1, list_lack[0])
    else:
        print(-1, -1)


if __name__ == '__main__':
    main()
