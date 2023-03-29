import requests
import re

url = input().strip()

res = requests.get(url)
url_text = res.text

# pattern = r'<a[^>]*?href=["\']?(?:.*://)?(\w[\w\.-]*?)[/:"\'][^>]*?>'
# pattern = r'<a[^>]*?href=["\']?(?:[^>]*://)?(\w[\w\.-]*)'
pattern = r'<a.*?href=["\']?(?:[^>^/]*://)?(\w[\w\.-]*)'

L = re.findall(pattern, url_text)

L2 = list(set(L))
L2.sort()
print(*L2, sep='\n')

# https://stepik.org/lesson/24471/step/7?auth=login&unit=6780
