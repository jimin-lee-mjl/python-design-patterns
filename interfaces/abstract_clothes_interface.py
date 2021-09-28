from abc import ABCMeta, abstractstaticmethod


class DeveloperSetupInterface(metaclass=ABCMeta):
    "Abstract interface for developer setup clothes factory"

    @abstractstaticmethod
    def get_setup(sizes):
        "calls hoody and jean factory methods"
