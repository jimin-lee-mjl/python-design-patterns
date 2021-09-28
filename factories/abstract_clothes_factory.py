from interfaces.abstract_clothes_interface import DeveloperSetupInterface
from factories.concrete_item_factory import JeanFactory, HoodieFactory


class DeveloperSetupFactory(DeveloperSetupInterface):
    "The abstract factory class for Hoodie and Jean factory classes"

    @staticmethod
    def get_setup(sizes):
        hoodie_size = sizes[0]
        jean_size = sizes[1]

        hoodie = HoodieFactory.create_object(hoodie_size)
        jean = JeanFactory.create_object(jean_size)

        return hoodie, jean
