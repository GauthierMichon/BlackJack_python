class Cards():
    def __init__(self, cardList, cardCount):
        self.cardList = cardList
        self.cardCount = cardCount

    def draw(self):
        cardDraw = self.cardList[0]
        self.cardList.pop(0)
        self.cardList.append(cardDraw)
        return cardDraw
