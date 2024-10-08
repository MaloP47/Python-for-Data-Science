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
        """Special method for visualization"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Special method for visualization as dev"""
        return self.__str__()


class Lannister(Character):
    """A Lannister always pays his debts"""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """Special method for visualization"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Special method for visualization as dev"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to instatiate a new object of class"""
        return cls(first_name, is_alive)
