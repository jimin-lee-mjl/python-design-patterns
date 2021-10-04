class 피카츄:
    """구상 클래스 Concrete Creator"""
    pass 

class 파이리:
    pass

class 꼬부기:
    pass

class 이상해씨:
    pass


class 포켓볼:
    def get_pokemon(self, type) -> """Concrete Product""":
        """Creator method"""
        if type == 'eletronic':
            return 피카츄()
        elif type == 'fire':
            return 파이리()
        elif type == 'water':
            return 꼬부기()
        elif type == 'grass':
            return 이상해씨()
