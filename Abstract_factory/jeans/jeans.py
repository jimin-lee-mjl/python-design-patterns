from interfaces.concrete_item_interface import JeanInterface


class LargeJean(JeanInterface):
    "JeanInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Large size jean"

    def __str__(self):
        return self.name

    def get_size(self):
        waist = 33
        length = 110
        return f'waist {waist}inch, length {length}cm'


class MediumJean(JeanInterface):
    "JeanInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Medium size jean"

    def __str__(self):
        return self.name

    def get_size(self):
        waist = 30
        length = 105
        return f'waist {waist}inch, length {length}cm'

    
class SmallJean(JeanInterface):
    "JeanInterface를 구현하고 있는 concrete class"

    def __init__(self):
        self.name = "Small size jean"

    def __str__(self):
        return self.name

    def get_size(self):
        waist = 27
        length = 100
        return f'waist {waist}inch, length {length}cm'
