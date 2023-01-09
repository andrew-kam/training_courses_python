def height(n: int, list_height: list[int]):
    list_chet, list_no = [], []
    for i in range(n):
        if i % 2 == 0 and list_height[i] % 2 == 0:
            list_chet.append(i+1)
    for i in range(n):
        if i % 2 == 1 and list_height[i] % 2 == 1:
            list_no.append(i+1)
    return list_chet, list_no


if __name__ == '__main__':
    number_students = int(input())
    list_height_students = list(map(int, input().split()))

    l_chet, l_no = height(number_students, list_height_students)

    if len(l_chet) == 1 and len(l_no) == 1:
        print(*l_chet, *l_no)
    else:
        print(-1, -1)
