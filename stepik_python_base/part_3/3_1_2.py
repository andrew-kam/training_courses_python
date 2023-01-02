s, t = (input() for _ in range(2))
n = 0
for i in range(len(s)):
#    if t == s[i:i+len(t)]:
    if s[i:].startswith(t):
        n += 1
print(n)
