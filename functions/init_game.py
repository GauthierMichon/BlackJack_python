from classes.person import Person
import random
from functions.clear import clear
from functions.init_deck import initDeck

def initGame() :
    clear()
    name = input("Comment t'appelles-tu ? ")
    player = Person(name, 0, [])
    nameListCroupier = ["Costa", "Kevin", "Jam", "Goat", "Michel"]
    nameCroupier = random.choice(nameListCroupier)
    croupier = Person(nameCroupier, 0, [])
    deck = initDeck()

    for i in range(3) :
        card = deck.draw()
        cardValue = card.getValue()
        if i%2 == 0:
            player.addCardToList(card)
            player.addToCountCardValue(cardValue)
        else :
            croupier.addCardToList(card)
            croupier.addToCountCardValue(cardValue)

    return player, croupier, deck


    