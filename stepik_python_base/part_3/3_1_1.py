s = input()
a = input()
b = input()
ans = 'Impossible'
if a not in s:
    ans = 0
else:
    for n in range(1000):
        s = s.replace(a, b)
        if a not in s:
            ans = n + 1
            break
print(ans)
