import requests
import re

# url_A = input()
# url_B = input()
url_A = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
url_B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
res = requests.get(url_A)
url_text = res.text
print(url_text)
list_1 = re.findall(r'a href="(https.*\.html)', url_text)
# print(list_1)

list_2 = []
for url in list_1:
    res = requests.get(url)
    if res.status_code == 200:
        url_text = res.text
       # print(url_text)
        list_2 += re.findall(r'a href="(https.*\.html)', url_text)
       # print(list_2)
if url_B in list_2:
    print('Yes')
else:
    print('No')

'''
start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")
'''