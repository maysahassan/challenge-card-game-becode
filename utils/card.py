<<<<<<< HEAD
class symbol:
    def __init__(self, icon, color):
        self.color = color
        self.icon = icon

    """def __str__(self):
        icon = ['\u2666', '\u2665', '\u2663', '\u2660']
        color = ["red", "black"]"""


class Card(symbol):

    def __init__(self, icon, color, value):
        super().__init__(icon, color)
        """value = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']"""
        self.value = value
        print("{}" "{}" "{}". format(self.icon, self.color, self.value))

yourcard = Card('\u2665', "red", 5)
print(yourcard)
=======
>>>>>>> 2734ce5afd6c8f5d2d3c84ff884d2797a5a87b31

