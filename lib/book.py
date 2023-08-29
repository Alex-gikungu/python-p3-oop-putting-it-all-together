class Book:
    def __init__(self, title="", page_count=0):
        self.title = title
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"

class Shoe:
    def __init__(self, brand="Unknown", size=0):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        self.condition = "New"
        return "Your shoe has been repaired."
