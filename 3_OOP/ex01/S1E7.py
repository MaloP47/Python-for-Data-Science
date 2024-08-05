"""3_OOP ex01"""

from S1E9 import Character


class Baratheon(Character):
    """Ours is the fury"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return self.__str__()

# class Lannister(Character):
#     """A Lannister always pays his debts"""
#     # Code