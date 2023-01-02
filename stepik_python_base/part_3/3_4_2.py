import json
names = []
js = json.loads(input())
dic = {}
for i in js:
    dic[i['name']] = i['parents']

dic_count = {}
for g in dic:
    dic_count[g] = 1
    for h in dic[g]:
        dic_count[h] = 1
sorted_dic = dict(sorted(dic_count.items()))

def search(dic, cl, pr):
    pr += (dic[cl])
    for i in dic[cl]:
        search(dic, i, pr)
    return pr

for j in dic:
    pr = list()
    pr = (search(dic, j, pr))
    pr_sort = list(set(pr))
    for k in sorted_dic:
        if k in pr_sort:
            sorted_dic[k] += 1

for v in sorted_dic:
    print(v, ':', sorted_dic[v])
