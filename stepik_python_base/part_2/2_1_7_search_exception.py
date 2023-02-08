def search(d, ls, err):
    global ANS
    if err in ls or d[err] in ls:
        ANS = True
    else:
        for j in d[err]:
            search(d, ls, j)


d = {}
for i in range(int(input())):
    st = input().split()
    if st[0] not in d:
        d[st[0]] = []
    if len(st) > 1:
        for j in range(2, len(st)):
            d[st[0]].append(st[j])
print(d)

ls = []
for j in range(int(input())):
    ls.append(input().strip())
print(ls)

for i in range(len(ls)):
    ANS = False
    err = ls[i]
    search(d, ls[:i], err)
    if ANS:
        print(err)

# https://stepik.org/lesson/24463/step/7?unit=6771
