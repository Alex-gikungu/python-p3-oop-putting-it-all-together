class Shoe:
    def __init__(self, brand="Unknown", size=0):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        self.condition = "New"
        return "Your shoe has been repaired."
