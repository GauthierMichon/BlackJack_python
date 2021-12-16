class Person():
    def __init__(self, name, countCardValue, cardList):
        self.name = name
        self.countCardValue = countCardValue
        self.cardList = cardList

    def addToCountCardValue(self, cardDraw) :
        if cardDraw == "As" :
            self.countCardValue += 11
        elif cardDraw == "Valet" or cardDraw == "Dame" or cardDraw == "Roi":
            self.countCardValue += 10
        else :
            self.countCardValue += int(cardDraw)
    
    def addCardToList(self, cardDraw) :
        self.cardList.append(cardDraw)

    def isLose(self) :
        if self.countCardValue > 21 :
            return True
        else :
            return False

    def AsValue(self) :
        if self.countCardValue > 21 :
            valueList = []
            for i in self.cardList :
                valueList.append(i.value)
            if "As" in self.cardList :
                newCountCardValue = 0
                countAs = 0
                for i in valueList :
                    if i == "Valet" or i == "Dame" or i == "Roi":
                        newCountCardValue += 10
                    elif i != "As" :
                        newCountCardValue += int(i)
                for i in valueList :
                    if i == "As" :
                        countAs += 1
                newCountCardValue += countAs
                for i in range(countAs) :
                    if newCountCardValue <= 11 :
                        newCountCardValue += 10

                self.countCardValue = newCountCardValue
        return self.countCardValue
