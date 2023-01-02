import requests
import json

client_id = '13c4d1b659c2a26164d2'
client_secret = '06909b2ae1c810c90ffa4f25dcd47d36'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]

art_list = []
headers = {"X-Xapp-Token": token}
with open('dataset_24476_4.txt') as file:
    for line in file:
        r = requests.get(f"https://api.artsy.net/api/artists/{line.strip()}", headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)
        # print(line, j['sortable_name'], j['birthday'])
        art_list.append(j['birthday'] + j['sortable_name'])
print(*art_list, sep='\n')
art_list.sort()
for art in art_list:
    print(art[4:])

# Astrolur
