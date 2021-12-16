from functions.clear import clear
from functions.init_game import initGame
from functions.print_info import printInfo

def game() :
    player, croupier, deck = initGame()
    booelan = True
    while booelan :

        printInfo(player, croupier)

        choiceboolean = False
        while not choiceboolean :
            choice = input("Voulez-vous tirer une nouvelle carte (O/N) ? ")
            if choice == "O" or choice == "N" :
                choiceboolean = True
            
        clear()
        if choice == "O" :
            card = deck.draw()
            cardValue = card.getValue()
            print("Vous avez pioché un(e) {0}.".format(card.display()))
            player.addCardToList(card)
            player.addToCountCardValue(cardValue)
            player.AsValue()
            input("Press enter to continue...")
            if player.isLose() :
                clear()
                print("Votre total de point est : {0}".format(player.countCardValue))
                print("Vous avez dépassé le maximum de 21.\n{0}, vous avez perdu contre le croupier {1}.".format(player.name, croupier.name))
                booelan = False
        
        else :
            croupierBoolean = True
            while croupierBoolean :
                clear()
                card = deck.draw()
                cardValue = card.getValue()
                print("Le croupier a pioché un(e) {0}.".format(card.display()))
                croupier.addCardToList(card)
                croupier.addToCountCardValue(cardValue)
                croupier.AsValue()
                print("Votre total de point est : {0}".format(player.countCardValue))
                print("Total de point du croupier : {0}".format(croupier.countCardValue))

                input("Press enter to continue...")
                if croupier.countCardValue >= 17 :
                    croupierBoolean = False

        if choice == "N" :
            booelan = False

    if croupier.isLose() :
        clear()
        print("Total de point du croupier : {0}".format(croupier.countCardValue))
        print("Le croupier a dépassé le maximum de 21.\n{0}, vous avez gagné contre le croupier {1}.".format(player.name, croupier.name))
        
    elif not player.isLose() :
        printInfo(player, croupier)
        if player.countCardValue > croupier.countCardValue :
            print("Vous avez plus de point que le croupier.\nFélicitation {0}, vous avez gagné contre le croupier {1}.".format(player.name, croupier.name))
        elif croupier.countCardValue > player.countCardValue :
            print("Vous avez moins de point que le croupier.\nMalheuresement {0}, vous avez perdu contre le croupier {1}.".format(player.name, croupier.name))
        else :
            print("Vous avez autant de point que le croupier.\n{0} c'est un match nul contre le croupier {1}.".format(player.name, croupier.name))
    

game()

