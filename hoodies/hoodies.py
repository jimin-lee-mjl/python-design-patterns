from interfaces.concrete_item_interface import HoodieInterface


class LargeHoodie(HoodieInterface):
    "HoodieInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Large size hoodie"

    def __str__(self):
        return self.name

    def get_size(self):
        width = 52
        length = 70
        return f'width {width}cm, length {length}cm'


class MediumHoodie(HoodieInterface):
    "HoodieInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Medium size hoodie"

    def __str__(self):
        return self.name

    def get_size(self):
        width = 48
        length = 65
        return f'width {width}cm, length {length}cm'

    
class SmallHoodie(HoodieInterface):
    "HoodieInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Small size hoodie"

    def __str__(self):
        return self.name

    def get_size(self):
        width = 44
        length = 60
        return f'width {width}cm, length {length}cm'
