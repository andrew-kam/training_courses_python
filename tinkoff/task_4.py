def rank(list_item: list[int]) -> list[list[int]]:
    rank_max = len(str(max(list_item)))
    list_rank = [list() for _ in range(rank_max)]
    for item in list_item:
        for i in range(len(str(item))):
            list_rank[i].append(item % 10) if item % 10 < 9 else ''
            item = item // 10
    for j in list_rank:
        j.sort()
    list_rank.reverse()
    return list_rank


def diff_sum(list_rank: list[list[int]], k: int) -> int:
    rank_max = len(list_rank)
    all_sum = 0
    for item in list_rank:
        for i in item:
            if k == 0:
                return all_sum
            all_sum += (9 - i) * (10 ** (rank_max - 1))
            k -= 1
        rank_max -= 1
    return all_sum


if __name__ == '__main__':
    n, attempt = map(int, input().split())
    list_numbers = list(map(int, input().split()))

    print(diff_sum(rank(list_numbers), attempt))

    # n, attempt = 11, 16
    # list_numbers = [1, 9899, 2, 1, 9235, 5, 99, 9, 85, 741, 34]
    # list_fig_int = [int(x) for x in list_fig]
    # list_fig_int = [1, 2, 1, 3, 5]
    # list_fig_int = [9999]
