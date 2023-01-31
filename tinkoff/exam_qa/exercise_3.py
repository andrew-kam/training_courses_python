def read_input():
    n = int(input())
    list_chief = []
    for i in range(n-1):
        list_chief.append(list(map(int, input().strip().split())))
    list_opinion = list(map(int, input().strip().split()))
    return n, list_chief, list_opinion


def get_answer(n, list_chief, list_opinion):
    if len(set(list_opinion)) == 1:
        return n
    count = 0
    chief_out = None
    for chief in list_chief:
        if list_opinion[chief[0] - 1] != list_opinion[chief[1] - 1]:
            count += 1
            chief_out = chief[1]
    if count == 1:
        return chief_out
    return False


def main():
    n, list_chief, list_opinion = read_input()
    answer = get_answer(n, list_chief, list_opinion)
    if answer:
        print("YES")
        print(answer)
    else:
        print("NO")


if __name__ == '__main__':
    main()
