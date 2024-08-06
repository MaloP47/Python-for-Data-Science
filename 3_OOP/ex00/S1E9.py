"""3_OOP ex00"""

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change health status"""
        self.is_alive = False


class Stark(Character):
    """Winter is coming"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Child class constructor"""
        super().__init__(first_name, is_alive)
