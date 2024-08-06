"""3_OOP ex02"""

from S1E7 import Baratheon, Lannister


# class King(Lannister, Baratheon):
class King(Baratheon, Lannister):
    """
    I'll tell you what. I'm going to give you a present.
    After I raise my armies, and kill your traitor brother,
    I'll give you his head as well.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """King constructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Sets eye color"""
        self.eyes = color

    def set_hairs(self, shade: str):
        """Sets hair shade of colour"""
        self.hairs = shade

    def get_eyes(self) -> str:
        """Getter for eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """Getter for hairs"""
        return self.hairs
