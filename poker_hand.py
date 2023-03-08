from card import Card


class PokerHand:
    def __init__(self, card_list: list):
        self.cards = card_list.copy()

    def add_card(self, card: Card):
        """
        Add card to deck
        :param card: Card instance
        :return: None
        """
        self.cards.append(card)

    def __Flush(self):
        """
        Checks if all cards have the same suit
        :return: True if the cards form a flush else False
        """
        suit = self.cards[0].get_suit()
        for card in self.cards[1:]:
            if card.get_suit() != suit:
                return False
        return True

    def score(self):
        """
        It calculates the score of a hand on a continuous scale
        score 2-14: for high card
        score 15-27: for one pair
        score 28-40: for two pair
        score 41-53: for a flush
        :return: score of the current hand based on the conditions
        """
        D = {}
        for card in self.cards:
            if card.get_rank() not in D:
                D[card.get_rank()] = 1
            else:
                D[card.get_rank()] += 1

        # A pair or two pairs
        if (len(D) == 4 or len(D) == 3) and max(D.values()) == 2:
            pair_ranks = []
            for rank, count in D.items():
                if count == 2:
                    pair_ranks.append(rank)
            _score = 13*len(pair_ranks) + max(pair_ranks)
        # A Flush
        elif self.__Flush():
            _score = 39 + max(D.keys())
        # High Card
        else:
            _score = max(D.keys())

        return _score

    def compare_to(self, other):
        """
        Determines how this hand compares to another hand, returns
        positive, negative, or zero depending on the comparison.
        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: a negative number if self is worth LESS than other, zero
        if they are worth the SAME, and a positive number if self is
        worth MORE than other
        """
        return self.score() - other.score()

    def clear(self):
        """
        Clears hand
        :return: None
        """
        self.cards.clear()

    def __str__(self):
        return str([str(card) for card in self.cards])







