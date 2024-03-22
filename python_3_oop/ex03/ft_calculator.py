
class calculator:

    def __init__(self, my_list) -> None:
        self.my_list = my_list

    def __add__(self, object) -> None:
        self.my_list = [x + object for x in self.my_list]
        print(self.my_list)

    def __mul__(self, object) -> None:
        self.my_list = [x * object for x in self.my_list]
        print(self.my_list)

    def __sub__(self, object) -> None:
        self.my_list = [x - object for x in self.my_list]
        print(self.my_list)

    def __truediv__(self, object) -> None:
        if (object == 0):
            print("Error: division by 0 is not allowed")
        else:
            self.my_list = [x / object for x in self.my_list]
            print(self.my_list)
