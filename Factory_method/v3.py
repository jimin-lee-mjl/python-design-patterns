from abc import ABCMeta


class 포켓몬(metaclass=ABCMeta):
    """포켓몬들의 추상 인터페이스 Product Interface"""
    pass

class 피카츄(포켓몬):
    """구상 클래스 Concrete Creator"""
    pass 

class 파이리(포켓몬):
    pass

class 꼬부기(포켓몬):
    pass

class 이상해씨(포켓몬):
    pass

class 라이츄(포켓몬):
    pass 

class 리자몽(포켓몬):
    pass

class 어니부기(포켓몬):
    pass

class 이상해꽃(포켓몬):
    pass


class 포켓몬팩토리:
    @staticmethod
    def get_pokemon(type) -> 포켓몬:
        if type == 'eletronic':
            return 피카츄()
        elif type == 'fire':
            return 파이리()
        elif type == 'water':
            return 꼬부기()
        elif type == 'grass':
            return 이상해씨()


class 진화한포켓몬팩토리:
    @staticmethod
    def get_pokemon(type) -> 포켓몬:
        if type == 'eletronic':
            return 라이츄()
        elif type == 'fire':
            return 리자몽()
        elif type == 'water':
            return 어니부기()
        elif type == 'grass':
            return 이상해꽃()


def provide_pokemon_factory(level):
    factories = {
        'basic': 포켓몬팩토리,
        'evolved': 진화한포켓몬팩토리
    }

    return factories[level]


class 포켓볼:        
    def get_pokemon(self, level, type) -> 포켓몬:
        return provide_pokemon_factory(level).get_pokemon(type) 
