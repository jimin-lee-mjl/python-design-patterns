import random
import random
from factory import get_pokeball

ball_options = {
    'yellow': '노란색',
    'green': '초록색',
    'red': '빨간색',
}


class User:
    def __init__(self, balance):
        self.balance = balance
        self.options = ['yellow', 'green', 'red']
        self.pokemons = []

    def buy_pokeball(self):
        option = random.choice(self.options)
        print(f'{ball_options[option]} 포켓볼을 구매합니다.')

        pokeball = get_pokeball(self.balance, option)
        if pokeball:
            self.pokemons.append(pokeball.get_pokemon())
            self.balance -= pokeball.price

    def retrieve_pokemons(self):
        for pokemon in self.pokemons:
            print(f'{pokemon}을(를) 가지고 있습니다.')


def main(money):
    user = User(money)
    balance = True

    print(f'{money}원으로 포켓볼 구매를 시작합니다.')
    print('--------------------------------')

    while balance:
        user.buy_pokeball()
        print(f'잔액이 {user.balance}원 남았습니다.')
        print('')
        
        if user.balance < 30000:
            balance = False

    print('--------------------------------')
    print('결과를 출력합니다.')
    user.retrieve_pokemons() 


main(100000)
