from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False


class Lannister(Character):

    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for classmethod"""
        return (cls(first_name, is_alive))
