
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}". format(self.value, self.suit))
        pass

card = Card("Card", 6)
card.show()

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        pass




