def count_digit(min_digit: int, max_digit: int) -> int:
    count = 0
    rank_min_digit = len(str(min_digit))
    rank_base = int('1' * rank_min_digit)
    while True:
        for digit in range(1, 10):
            if min_digit <= digit * rank_base <= max_digit:
                count += 1
            elif digit * rank_base > max_digit:
                return count
        rank_base = int(f'{str(rank_base)}{1}')


if __name__ == "__main__":
    l, r = map(int, input().split())
    print(count_digit(l, r))
