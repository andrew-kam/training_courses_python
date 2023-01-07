n, t = map(int, input().split())
list_floor = list(map(int, input().split()))
e = int(input())

if __name__ == '__main__':
    min_diff = (
        list_floor[e - 1] - list_floor[0]
        if list_floor[e - 1] - list_floor[0] < list_floor[-1] - list_floor[e - 1]
        else list_floor[-1] - list_floor[e - 1]
    )

    print(
        list_floor[-1] - list_floor[0]
        if list_floor[e - 1] - list_floor[0] <= t
        or list_floor[- 1] - list_floor[e - 1] <= t
        else list_floor[-1] - list_floor[0] + min_diff
    )
