s, t = (input() for _ in range(2))
n = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        n += 1
print(n)

# https://stepik.org/lesson/24469/step/7?unit=6775
