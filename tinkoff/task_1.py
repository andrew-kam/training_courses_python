a, b, c, d = map(int, input().split())

if __name__ == '__main__':
    print(a if d <= b else a + (d - b) * c)

# 100  10  12  15 / 160
# 100  10  12  1 / 100
