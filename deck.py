from card import Card
import random


class Deck:
    # Name of suits
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

    def __init__(self):
        self.cards = []
        for r in range(2, 15):
            for s in Deck.suits:
                self.cards.append(Card(rank=r, suit=s))

    def deal(self):
        """
        Deal card from the deck
        :return:
        """
        return self.cards.pop(0)

    def shuffle(self):
        """
        Shuffle the deck
        :return:
        """
        random.shuffle(self.cards)
