def read_input() -> tuple[int, list[int]]:
    sum_coins = int(input().strip())
    coins = list(map(int, input().strip().split()))
    return sum_coins, coins


def get_answer_3(sum_coins: int, coins: list[int]) -> int:
    sum_coins -= 1
    count = 1
    max_coin = max(coins)
    min_coin = min(coins)
    coins.remove(min_coin)
    coins.remove(max_coin)
    middle_coin = coins[0]
    max_len = int(sum_coins / min_coin) + 2
    for i in range(max_len):
        if max_coin * i > sum_coins:
            break
        elif i > 0:
            count += 1
        for j in range(max_len):
            if max_coin * i + middle_coin * j > sum_coins:
                break
            elif j > 0:
                count += 1
            count += int((sum_coins - (max_coin * i + middle_coin * j)) / min_coin)
    return count


def get_answer_2(sum_coins: int, coins: list[int]) -> int:
    sum_coins -= 1
    count = 1
    max_coin = max(coins)
    min_coin = min(coins)
    max_len = int(sum_coins / min_coin) + 2
    for i in range(max_len):
        if max_coin * i > sum_coins:
            break
        elif i > 0:
            count += 1
        count += int((sum_coins - max_coin * i) / min_coin)
    return count


def main():
    sum_coins, coins = read_input()
    if coins[0] == coins[1] == coins[2]:
        sum_coins -= 1
        print(int(sum_coins / coins[0]) + 1)
    elif coins[0] == coins[1] or coins[0] == coins[2] or coins[1] == coins[2]:
        print(get_answer_2(sum_coins, coins))
    else:
        print(get_answer_3(sum_coins, coins))


if __name__ == '__main__':
    main()

    assert get_answer_3(15, [4, 7, 9]) == 9

# 0 0 0
# 0 0 1
# 0 0 2
# 0 0 3
# 0 1 1
# 0 2 0
# 1 0 1

# 0 1 0

# 1 0 0
