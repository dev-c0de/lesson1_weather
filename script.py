import requests


def get_weather(places):
    url = 'https://wttr.in/'
    payload = {
        "n": "",
        "T": "",
        "q": "",
        "M": "",
        "lang": "ru"
    }
    for place in places:
        response = requests.get(f'{url}{place}', params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    get_weather(['Лондон', 'Шереметьево', 'Череповец'])
