import requests
import re

url_A = input()
url_B = input()

res = requests.get(url_A)
url_text = res.text
list_1 = re.findall(r'a href="(https.*\.html)', url_text)

list_2 = []
for url in list_1:
    res = requests.get(url)
    if res.status_code == 200:
        url_text = res.text
        list_2 += re.findall(r'a href="(https.*\.html)', url_text)
if url_B in list_2:
    print('Yes')
else:
    print('No')

# https://stepik.org/lesson/24471/step/6?auth=login&unit=6780
