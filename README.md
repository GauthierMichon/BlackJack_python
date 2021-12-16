# Black Jack

## I. Card

Le but de cette partie est de créer une classe `card`.

![](https://i.imgur.com/DIjJEHe.png)

La classe `card` possède 2 attributs :
    - `value` qui va contenir la valeur de la carte.
    - `color` qui va contenir le signe de la carte.
    
    
La classe `card` possède 3 méthodes : 
    - `getValue` qui va récupérer la valeur de la carte.
    - `getColor` qui va récupérer le signe de la carte.
    - `display` qui va retourner la combinaison de la valeur et du signe dans le format `4♥`.
    
## II. Cards

Le but de cette partie est de créer une classe `cards`.

![](https://i.imgur.com/KOgW069.png)

La classe `cards` possède 2 attributs :
    - `cardList` qui va contenir la totalité des cartes du paquet.
    - `cardCount` qui va contenir le nombre de carte au total dans le paquet.
    
La classe `cards` possède 1 seule méthode : 
    - `draw` qui va retourner la première carte du paquet, et la mettre en dessous du paquet. Cette carte sera stocker dans la liste de carte du joueur. Cela pourrait donc sembler contradictoire de la remettre à la fin. C'est juste plus simple et cela m'évite de le faire à la fin de la partie
    
## III. Game

### Mes autres classes

#### La classe Person :
![](https://i.imgur.com/pT73VMg.png)
![](https://i.imgur.com/AzqAiGc.png)

La classe `Person` possède 3 attributs :
    - `name` qui va contenir le nom de la peronne.
    - `countCardValue` qui contenir le total de point de la personne.
    - `cardList` qui va contenir toutes les cartes tiré par la personne
    
La classe `Person` possède 4 méthodes : 
    - `addToCountValue` qui va ajouter la valeur de la carte au total de point de la personne.
    - `addCardToList` qui va ajouter la carte tiré à la liste de carte de la personne.
    - `isLose` qui va servir à savoir si la personne à dépasser le maximum de 21 points.
    - `AsValue` qui va servir à moduler la valeur de l'as.

### Mes fonctions

#### Fonction clear : 
![](https://i.imgur.com/9XU9GJJ.png)
Cette fonction sert à rafraîchir le terminal.

#### Fonction initDeck : 
![](https://i.imgur.com/hgJSuYm.png)
Cette fonction sert à initialiser le paquet de carte.
Je déclare tout d'abord 2 listes : 
![](https://i.imgur.com/IVBy7r0.png)
    - La première avec toutes les valeurs de carte possibles.
    - La Deuxième avec tous les signes de carte possibles.

![](https://i.imgur.com/0SZxqtO.png)
Ensuite je fais des boucles imbriqués pour faire une liste avec 8 paquets de 52 cartes. Soit un total de 416 cartes.

![](https://i.imgur.com/hoEpWvt.png)
Je mélange le paquet de carte.

![](https://i.imgur.com/xVFURcL.png)
Je stock le paquet dans un objet de type `Cards`.

#### Fontion initGame
![](https://i.imgur.com/UsW1h2u.png)

Cette fonction sert à initialiser les variables que l'on va utiliser tout au long du programme.

![](https://i.imgur.com/0UzKfW7.png)
On commence par clear le terminal.

![](https://i.imgur.com/T3bZnAs.png)
On demande son nom au joueur, puis on crée un Objet `Person` qui sera notre joueur et un autre Objet `Person` qui sera notre croupier.

![](https://i.imgur.com/287hi9c.png)
On initialise notre paquet de carte.

![](https://i.imgur.com/9PQKfln.png)
Je boucle 3 fois.
Dans chaque boucle, je tire une carte et je récupère sa valeur.
Selon le nombre j'ajoute la carte à player ou à croupier.

#### Fonction printInfo
![](https://i.imgur.com/TP0rEen.png)

Cette fonction sert à afficher les cartes et les points totaux de chaque joueurs.

![](https://i.imgur.com/ioZXuzb.png)
On récupère toutes les cartes du joueur et on les stocks dans une string.
On fait la même chose pour le croupier.

![](https://i.imgur.com/kqth8Gq.png)
On clear le terminal
Et on affiche toutes nos informations.

### Fonction de jeu
![](https://i.imgur.com/UOfmv9s.png)
![](https://i.imgur.com/cEWPGFK.png)
![](https://i.imgur.com/mLPhpgF.png)

Cette fonction va être le moteur de jeu.

![](https://i.imgur.com/sFfjlUX.png)
On récupère les données de notre Initiation de jeu.
On déclare un booléen qui va nous servir.

![](https://i.imgur.com/hrhLZsC.png)
On affiche nos informations.
Dans cette boucle, on fait choisir à l'utilisateur de tirer une nouvelle carte ou de s'arêter là.

![](https://i.imgur.com/98blYC2.png)
On clear le terminal.
Si l'utilisateur choisi de tirer une carte, il tire une carte, on affiche la carte tiré. On ajoute sa valeur au score de notre joueur et la carte à sa liste de carte.
On réajuste les valeurs des `As`.
Enfin on vérifie si le joueur à dépasser le score maximum de 21 points et si c'est la cas, on affiche les messages de défaite .

![](https://i.imgur.com/D0w7SpF.png)
On déclare un booléen qui va nous servir à faire tirer des cartes en boucle au croupier.
On clear le terminal.
Le croupier tire une carte, et comme pour le joueur on ajoute la carte à sa liste de carte et on ajoute sa valeur au score de notre croupier.
On réajuste les valeurs des `As`.
Enfin on vérifie si le croupier à dépasser le score de 17 points et si c'est la cas le croupier arrête de tirer des cartes
Si le joueur avait choisi de ne pas tirer de carte, le jeu s'arrête.

![](https://i.imgur.com/SsoRhBE.png)
On regarde si le croupier à dépasser le score maximum de 21 points et si c'est la cas, on affiche les messages de victoire .
Enfin si personne n'a dépasser les 21 points, on compare les scores pour voir qui a gagné.

![](https://i.imgur.com/0a3YwUc.png)
Et pour terminer le programme, on appelle la fonction de notre jeu.
