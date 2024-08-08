"""4_Dod ex03"""

# https://docs.python.org/3/library/dataclasses.html

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generates an id string"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Post constructor"""
        self.login = self.name[0] + self.surname
