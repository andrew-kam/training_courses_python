import requests

base_url = 'http://numbersapi.com/{}/math?json=true'
with open('dataset_24476_3.txt') as file:
    for line in file:
        url = base_url.format(line.strip())
        res = requests.get(url)
        data = res.json()
        print('Interesting' if data['found'] else 'Boring')

# https://stepik.org/lesson/24476/step/3?auth=login&unit=6781
