def read_input():
    n_set = int(input())
    items = list(map(int, input().strip().split()))
    n_request = int(input())
    list_request = []
    for i in range(n_request):
        list_request.append(list(map(int, input().strip().split())))

    return items, list_request


def apply_request(items, list_request):
    for request in list_request:
        if request[0] == 1:
            for i in range(len(items)):
                items[i] += request[1]
        if request[0] == 2:
            items.append(request[1])
        if request[0] == 3:
            items.remove(request[1])
        if request[0] == 0 and request[1] in items:
            print("Yes")
        if request[0] == 0 and request[1] not in items:
            print("No")


def main():
    items, list_request = read_input()
    apply_request(items, list_request)


if __name__ == '__main__':
    main()
