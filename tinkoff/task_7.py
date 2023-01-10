def check_cycle(list_items: list[int]) -> bool:
    i = 0
    ai = list_items[i]
    count = 1
    while ai != 1:
        i = ai
        ai = list_items[i - 1]
        count += 1
        if count > len(list_items):
            return False
    return True if count == len(list_items) else False


def double(list_items: list[int]):
    list_double = []
    list_not_in = []
    list_index = []
    for i in range(1, len(list_items) + 1):
        if i not in list_items:
            list_not_in.append(i)
        if list_items.count(i) == 2:
            list_double.append(i)
    if len(list_double) == 1:
        list_index = [i for i in range(len(list_items))
                      if list_items[i] == list_double[0]]
    return list_double, list_not_in, list_index


if __name__ == '__main__':
    number_students = int(input())
    list_students = list(map(int, input().split()))

    l_double, l_not_in, l_index = double(list_students)
    if len(l_double) == 1:
        y = l_not_in[0]
        ind_1 = l_index[0]
        ind_2 = l_index[1]

        list_new_1 = list_students[:]
        list_new_1[ind_1] = y

        list_new_2 = list_students[:]
        list_new_2[ind_2] = y

        if check_cycle(list_new_1):
            print(ind_1 + 1, y)

        elif check_cycle(list_new_2):
            print(ind_2 + 1, y)
        else:
            print(-1, -1)
    else:
        print(-1, -1)

# list_students = [2, 3, 4, 6, 1, 1]
    # print(check_cycle(list_students))
# print(check_cycle(list_new_1))
# print(check_cycle(list_new_2))
