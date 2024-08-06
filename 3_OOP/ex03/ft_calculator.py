"""3_OOP ex03"""


class calculator:
    """Class"""
    def __init__(self, vector) -> None:
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """add"""
        self.vector = [nb + object for nb in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiply"""
        self.vector = [nb * object for nb in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """substract"""
        self.vector = [nb - object for nb in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """divide"""
        if object == 0:
            raise ValueError("division by zero not allowed")
        self.vector = [nb / object for nb in self.vector]
        print(self.vector)
