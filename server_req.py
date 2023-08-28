import requests
from config import SERVER_URL


def add_to_leaderboard(self):
    data = {
        'name': self.user_name,
        'score': len(self.player.parts)
    }

    try:
        response = requests.post(SERVER_URL + '/player', json=data)
        print(response.text)
    except ConnectionError:
        print('connection error')


def check_name(self):
    print(f'{self.name}')


def get_leaderboard():
    try:
        url = SERVER_URL + '/leaderboard'
        return requests.get(url).json()
    except ConnectionError:
        print('connection error')
