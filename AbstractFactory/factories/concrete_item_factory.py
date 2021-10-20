from hoodies.hoodies import LargeHoodie, MediumHoodie, SmallHoodie
from jeans.jeans import LargeJean, MediumJean, SmallJean


class HoodieFactory:
    "The factory class"

    @staticmethod
    def create_object(size):
        if size == 'sm':
            return SmallHoodie()
        elif size == 'md':
            return MediumHoodie()
        elif size == 'lg':
            return LargeHoodie()


class JeanFactory:
    "The factory class"

    @staticmethod
    def create_object(size):
        if size == 'sm':
            return SmallJean()
        elif size == 'md':
            return MediumJean()
        elif size == 'lg':
            return LargeJean()