class Card():
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def display(self):
        return "{0}{1}".format(self.value, self.color)