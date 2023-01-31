def read_input():
    n = int(input())
    list_active = list(map(int, input().strip().split()))
    k = int(input())
    return n, list_active, k


def get_answer(list_active, k):
    count = 0
    for i in range(len(list_active)):
        for j in range(i+1, len(list_active)+1):
            k_active = len(set(list_active[i:j]))
            if k_active >= k:
                count += 1
    return count


def main():
    n, list_active, k = read_input()
    print(get_answer(list_active, k))


if __name__ == '__main__':
    main()
