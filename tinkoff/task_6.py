def height(list_height: list[int]):
    list_chet, list_no = [], []
    for i in range(len(list_height)):
        if i % 2 == 0 and list_height[i] % 2 == 0:
            list_chet.append(i+1)
        if i % 2 == 1 and list_height[i] % 2 == 1:
            list_no.append(i+1)
    return list_chet, list_no


def check(list_items: list, ind_chet: int, ind_no: int):
    list_new = list_items[:]
    list_new[ind_chet], list_new[ind_no] = list_new[ind_no], list_new[ind_chet]
    for i in range(len(list_new)):
        if i % 2 == 0 and list_new[i] % 2 == 0\
                or i % 2 == 1 and list_new[i] % 2 == 1:
            return False
    return True


if __name__ == '__main__':
    number_students = int(input())
    list_height_students = list(map(int, input().split()))

    l_chet, l_no = height(list_height_students)

    if len(l_chet) == len(l_no) == 1:
        if check(list_height_students, l_chet[0] - 1, l_no[0] - 1):
            print(*l_chet, *l_no)
    else:
        print(-1, -1)
