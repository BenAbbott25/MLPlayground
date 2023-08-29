# classes

# game table
# 1 standard deck, 2-4 players, each has a draw pile, discard pile, hand of 4 cards, health, shields, victory cards
# table has shop to buy new cards and a burn pile
# game ends when a player has 3 victory cards or all but 1 players is out of health
# players take turns, play any number of cards of the same type, then draw back up to 4 cards
# shop has deck of face down shuffled red cards, a deck of face down shuffled black cards, 2 of each victory card face up, 2 of each shield card face up
class Game:
    def __init__(self, deck, players, shop):
        self.deck = deck
        self.players = players
        self.shop = shop

    def start_game(self):
        # shuffle decks
        # deal starting hands
        # set up shop
        pass


    def end_game(self):
        pass

    def turn(self):
        pass

    def draw(self):
        pass

    def play(self):
        pass

    def discard(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def econ(self):
        pass

    def victory(self):
        pass

    def burn(self):
        pass

    def shuffle(self):
        pass


# player
# 40 health, hand
class Player:
    def __init__(self, name, health, hand):
        self.name = name
        self.health = health
        self.hand = hand

    def draw(self):
        pass

    def play(self):
        pass

    def discard(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def econ(self):
        pass

    def victory(self):
        pass

    def burn(self):
        pass

    def shuffle(self):
        pass


# Deck
    

# card
class Card:
    def __init__(self, name, card_type, value):
        self.name = name
        self.card_type = card_type
        self.value = value

# card types by inheritance
class Attack(Card):
    # Black number cards, deal damage equal to their face value
    def __init__(self, name, card_type, value):
        super().__init__(name, card_type, value)

class Econ(Card):
    # Red number cards, worth their face value
    def __init__(self, name, card_type, value):
        super().__init__(name, card_type, value)

class Shield(Card):
    # Black Face cards, block 5,10,15 damage cost 10,15,20
    def __init__(self, name, card_type, value):
        super().__init__(name, card_type, value)

class Victory(Card):
    # Red Face cards, collecting one of each is an instant win. cost 25,30,35
    def __init__(self, name, card_type, value):
        super().__init__(name, card_type, value)


redMain = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "AH"
           "2D", "3D", "4D","5D", "6D", "7D", "8D", "9D", "10D", "AD"]
blackMain = ["2C", "3C", "4C","5C", "6C", "7C", "8C", "9C", "10C", "AC"
             "2S", "3S", "4S","5S", "6S", "7S", "8S", "9S", "10S", "AS"]
victory = ["JH", "QH", "KH", "JD", "QD", "KD"]
shield = ["JS", "QS", "KS", "JC", "QC", "KC"]


# assign cards
for card in redMain:
    card = Econ(card, "red numbers", card[:-1])

for card in blackMain:
    card = Attack(card, "black numbers", card[:-1])

for card in victory:
    card = Victory(card, "victory")

for card in shield:
    # values: J = 5, Q = 10, K = 15
    card = Shield(card, "shield", {"J": 5, "Q": 10, "K": 15}[card[:-1]])


