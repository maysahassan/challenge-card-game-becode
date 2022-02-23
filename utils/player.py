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
        print(f"Your card is", "Nano", card)


class Deck:

    def __init__(self):
        self.cards = []
        self.fill_deck()
        """self.show()"""
        self.shuffle()
        self.distribute()

    def fill_deck(self):
        for s in ['\u2666', '\u2665', '\u2663', '\u2660']:
            for v in range(1, 14):
                self.cards.append(Card(s, v, ""))
        return self

    """def show(self):
        for c in self.cards:
            c.show()"""

    def shuffle(self):

        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            return self

    def distribute(self):
        self.cards.pop()
        return self


deck = Deck()
card1 = deck.shuffle()
card2 = deck.distribute()
print(card1, card2)
