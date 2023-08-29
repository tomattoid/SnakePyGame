import requests
from config import SERVER_URL


class ServerReq():
    def __init__(self, user_name=None, score=None):
        self.user_name = user_name
        self.score = score

    def add_to_leaderboard(self):
        if self.user_name is None or self.score is None:
            print("missing user_name or score")
            return

        data = {
            'name': self.user_name,
            'score': self.score
        }

        try:
            response = requests.post(SERVER_URL + '/player', json=data)
            print(response.text)
        except ConnectionError:
            print('connection error')

    def check_name(self):
        print(f'{self.name}')

    def get_leaderboard(self):
        try:
            url = SERVER_URL + '/leaderboard'
            return requests.get(url).json()
        except ConnectionError:
            print('connection error')
