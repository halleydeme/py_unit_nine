class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __str__(self):
        return self.rank + " of " + self.suit

    def __gt__(self, other):
        if (self.rank == other.rank):
            return self.suits.index(self.suit) > other.suits.index(other.suit)
        else:
            return self.ranks.index(self.rank) > other.ranks.index(other.rank)