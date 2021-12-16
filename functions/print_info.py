from functions.clear import clear

def printInfo(player, croupier) :
    cardListPlayerToPrint = ""
    for i in player.cardList :
        cardListPlayerToPrint += "{0}, ".format(i.display())
    cardListPlayerToPrint = cardListPlayerToPrint[:-2]

    cardListCroupierToPrint = ""
    for i in croupier.cardList :
        cardListCroupierToPrint += "{0}, ".format(i.display())
    cardListCroupierToPrint = cardListCroupierToPrint[:-2]

    clear()
    
    print("Vos cartes sont : {0}".format(cardListPlayerToPrint))
    print("Total de vos point : {0}".format(player.countCardValue))
    print("Les cartes du croupier sont : {0}".format(cardListCroupierToPrint))
    print("Total de point du croupier : {0}".format(croupier.countCardValue))