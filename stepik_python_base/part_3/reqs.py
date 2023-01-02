import requests

'''
res = requests.get('https://docs.python.org/3.5/')
print(res.status_code)
print(res.headers['Content-Type'])
print(res.content)
print(res.text)
'''

'''
res = requests.get('https://docs.python.org/3.5/_static/py.png')
print(res.status_code)
print(res.headers['Content-Type'])
print(res.content)

with open("python.png", "wb") as f:
    f.write(res.content)
'''

res = requests.get("https://yandex.ru/search/",
                   params={
                       "text": "Stepic",
                       "test": "test1",
                       "name": "Name With Spaces",
                       "list": ["test1", "test2"]
                   })
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
# print(res.text)
