# Corrected Shoe class
class Shoe:
    def __init__(self, brand="Unknown", size=0):
        self.brand = brand
        self._size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        return "Your shoe has been repaired."