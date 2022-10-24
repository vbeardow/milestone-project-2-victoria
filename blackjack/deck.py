import random
from blackjack.constants import suits, ranks
from blackjack.card import Card


class Deck:
    """A class representing a deck of 52 cards"""

    def __init__(self) -> None:
        """Constructs the deck of cards with a single card of each suit/rank"""
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self) -> str:
        """Returns a list of cards within the deck

        Returns:
            List[str]: a list of names of cards within the deck e.g. "Two of Hearts"
        """
        card_list = ""
        for card in self.deck:
            card_list += (card.__str__()) + "\n"
        return card_list

    def shuffle(self) -> None:
        """Randomly shuffles the deck of cards"""
        random.shuffle(self.deck)

    def deal(self) -> Card:
        """Deals a single card off the deck of cards

        Returns:
            Card: A single card that gets dealt from the deck
        """
        return self.deck.pop()
