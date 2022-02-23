<<<<<<< HEAD
from utils.card import Card
import random

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = [Card('\u2660', "black", 3), Card('\u2665', "black", 5), Card('\u2662', "black", 8)]
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def __str__(self):
        return self.cards

    def play(self):
        card = random.choice(self.cards)
        self.history.append(card)
        pname1 = Player("nano")
        print(f"Your card is", pname1, card)


class Deck:

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for s in ['\u2666', '\u2665', '\u2663', '\u2660']:
            for v in range(1, 14):
                self.cards.append(Card(s, v, ""))

    def show(self):
        for c in self.cards:
            c.show()


deck = Deck()
deck.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
             r = random.randint(0, i)
             self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    deck = Deck()
    deck.shuffle()
    deck.show()
=======
>>>>>>> 2734ce5afd6c8f5d2d3c84ff884d2797a5a87b31

