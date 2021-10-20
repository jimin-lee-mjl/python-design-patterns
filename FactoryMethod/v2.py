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


class 포켓몬팩토리:
    @staticmethod
    def get_pokemon(type) -> 포켓몬:
        """Creator method"""
        if type == 'eletronic':
            return 피카츄()
        elif type == 'fire':
            return 파이리()
        elif type == 'water':
            return 꼬부기()
        elif type == 'grass':
            return 이상해씨()


class 포켓볼:
    def get_pokemon(self, type) -> 포켓몬:
        return 포켓몬팩토리.get_pokemon(type)
