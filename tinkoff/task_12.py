def read_input() -> tuple[int, list[int]]:
    sum_coins = int(input().strip())
    coins = list(map(int, input().strip().split()))
    return sum_coins, coins


def get_answer(sum_coins: int, coins: list[int]) -> int:
    sum_coins -= 1
    count = 0
    max_coin = max(coins)
    min_coin = min(coins)
    coins.remove(min_coin)
    coins.remove(max_coin)
    middle_coin = coins[0]
    max_len = int(sum_coins / min_coin) + 2
    for i in range(max_len):
        if max_coin * i > sum_coins:
            break

        for j in range(max_len):
            if max_coin * i + middle_coin * j > sum_coins:
                break

            for k in range(max_len):
                if max_coin * i + middle_coin * j + min_coin * k > sum_coins:
                    break
                count += 1

    return count


def main():
    sum_coins, coins = read_input()
    print(get_answer(sum_coins, coins))


if __name__ == '__main__':
    main()

    assert get_answer(15, [4, 7, 9]) == 9

# 0 0 0
# 0 0 1
# 0 0 2
# 0 0 3
# 0 1 1
# 0 2 0
# 1 0 1

# 0 1 0

# 1 0 0
