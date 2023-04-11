import requests

places = ['Лондон', 'Шереметьево', 'Череповц']
url = 'https://wttr.in/'
payload = {"lang": "ru"}
for place in places:
    response = requests.get(url+place+'?nTqm', params=payload)
    response.raise_for_status()
    print(response.text)
