from abc import ABCMeta, abstractstaticmethod


class HoodieInterface(metaclass=ABCMeta):
    "Interface for Hoodie classes"

    @abstractstaticmethod
    def get_size():
        "returns hoodie sizes"


class JeanInterface(metaclass=ABCMeta):
    "Interface for Jean classes"

    @abstractstaticmethod
    def get_size():
        "returns jean sizes"
