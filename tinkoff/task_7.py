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


def main():
    # len_student, students = read_input()
    students = [2, 3, 4, 5, 6, 4]
    print(checker(students))
    list_double, list_lack, indexes_double = double(students)
    print(double(students))
    if len(indexes_double) == 2:
        index_1 = indexes_double[0]
        index_2 = indexes_double[1]
        students_new_1 = students[:]
        students_new_1[index_1] = list_lack[0]
        students_new_2 = students[:]
        students_new_2[index_2] = list_lack[0]
        if checker(students_new_1):
            print(index_1 + 1, list_lack[0])
        elif checker(students_new_2):
            print(index_2 + 1, list_lack[0])
        else:
            print(-1, -1)


if __name__ == '__main__':
    main()

    # l_double, l_not_in, l_index = double(list_students)
    # if len(l_double) == 1:
    #     y = l_not_in[0]
    #     ind_1 = l_index[0]
    #     ind_2 = l_index[1]
    #
    #     list_new_1 = list_students[:]
    #     list_new_1[ind_1] = y
    #
    #     list_new_2 = list_students[:]
    #     list_new_2[ind_2] = y
    #
    #     if check_cycle(list_new_1):
    #         print(ind_1 + 1, y)
    #
    #     elif check_cycle(list_new_2):
    #         print(ind_2 + 1, y)
    #     else:
    #         print(-1, -1)
    # else:
    #     print(-1, -1)

# list_students = [2, 3, 4, 6, 1, 1]
# print(check_cycle(list_students))
# print(check_cycle(list_new_1))
# print(check_cycle(list_new_2))
