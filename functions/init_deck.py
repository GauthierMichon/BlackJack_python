from classes.card import Card
import random
from classes.cards import Cards

def initDeck() :
    listValue = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    listColor = ["♥", "♦", "♣", "♠"]

    deckList = []

    for _ in range(8) :
        for val in listValue :
            for col in listColor :
                deckList.append(Card(val, col))

    random.shuffle(deckList)
    deck = Cards(deckList, len(deckList))
    return deck



