from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Abstract Class"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Your docstring for Abstract Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for Abstract Method"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
