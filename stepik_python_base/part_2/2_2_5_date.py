import datetime


def read_input():
    year, month, day = map(int, input().strip().split())
    delta = datetime.timedelta(days=int(input().strip()))
    return year, month, day, delta


def get_answer(year, month, day, delta):
    current_date = datetime.date(year, month, day)
    new_date = current_date + delta
    return new_date


def main():
    answer_date = get_answer(*read_input())
    print(answer_date.year, answer_date.month, answer_date.day)


if __name__ == '__main__':
    main()
