import requests
import re

# url = input().strip()
url = 'https://pastebin.com/raw/7543p0ns'

res = requests.get(url)
url_text = res.text
# print(url_text)
# pattern = r'<a[^>]*?href=["\']?(?:.*://)?(\w[\w\.-]*?)[/:"\'][^>]*?>'
# pattern = r'<a[^>]*?href=["\']?(?:[^>]*://)?(\w[\w\.-]*)'
pattern = r'<a.*?href=["\']?(?:[^>^/]*://)?(\w[\w\.-]*)'

L = re.findall(pattern, url_text)

L2 = list(set(L))
L2.sort()
print(*L2, sep='\n')
