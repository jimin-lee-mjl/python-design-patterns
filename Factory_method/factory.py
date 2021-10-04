import random


class YellowBall:
    def __init__(self):
        self.color = '노란색'
        self.price = 30000
        self.options = ['피츄', '파이리', '꼬부기', '이상해씨']

    def get_pokemon(self):
        pokemon = random.choice(self.options)
        print(f'{self.color} 포켓볼을 열었습니다.')
        print(f'{pokemon}를 획득했습니다.')
        return pokemon
        

class GreenBall:
    def __init__(self):
        self.color = '초록색'
        self.price = 50000
        self.options = ['피카츄', '리자드', '어니부기', '이상해풀']

    def get_pokemon(self):
        pokemon = random.choice(self.options)
        print(f'{self.color} 포켓볼을 열었습니다.')
        print(f'{pokemon}을(를) 획득했습니다.')
        return pokemon


class RedBall:
    def __init__(self):
        self.color = '빨간색'
        self.price = 70000
        self.options = ['라이츄', '리자몽', '거북왕', '이상해꽃']

    def get_pokemon(self):
        pokemon = random.choice(self.options)
        print(f'{self.color} 포켓볼을 열었습니다.')
        print(f'{pokemon}을(를) 획득했습니다.')
        return pokemon


def get_pokeball(balance, ball_type):

    """factory"""
    pokeballs = {
        "yellow": YellowBall(),
        "green": GreenBall(),
        "red": RedBall(),
    }

    pokeball = pokeballs[ball_type]

    if balance < pokeball.price:
        print('잔액이 부족합니다.')
        return False

    print(f'{pokeball.color} 포켓볼을 구매했습니다.')
    return pokeball
