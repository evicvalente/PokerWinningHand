class Card:
    rank_to_name = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}

    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        """
        Get rank of card
        :return:
        """
        return self.rank

    def get_suit(self):
        """
        Get suit of card
        :return:
        """
        return self.suit

    def __str__(self):
        """
        String representation of Card
        :return: str of card
        """
        if self.rank in Card.rank_to_name:
            return Card.rank_to_name.get(self.rank) + '-' + self.suit
        else:
            return str(self.rank) + '-' + self.suit
