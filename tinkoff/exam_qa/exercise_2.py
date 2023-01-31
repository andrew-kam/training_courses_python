def read_input():
    n = int(input())
    s = input().strip()
    return s


def checker(s):
    return len(s) % 2 == 0 and s[:int(len(s)/2)] == s[int(len(s)/2):]


def get_answer(s):
    if len(s) % 2 == 0:
        s_1 = s[:int(len(s)/2)]
        s_2 = s[int(len(s)/2):]
    else:
        return False
    count = 0
    list_item_1 = []
    list_item_2 = []
    for i in range(len(s_1)):
        if s_1[i] != s_2[i]:
            count += 1
            list_item_1.append(s_1[i])
            list_item_2.append(s_2[i])
            if count > 2:
                return False
    if count == 2 and list_item_1[0] == list_item_2[1] and list_item_1[1] == list_item_2[0]:
        return True
    return False


def main():
    s = read_input()
    print("YES" if checker(s) or get_answer(s) else "NO")


if __name__ == '__main__':
    main()
