def read_input():
    s = input().strip()
    return s[0], s[1]


def get_answer(s):
    return (s[0].isdigit() and s[1].isalpha()) \
        or (s[1].isdigit() and s[0].isalpha())


def main():
    s = read_input()
    print("YES" if get_answer(s) else "NO")


if __name__ == '__main__':
    main()
