from blackjack.hand import Hand
from blackjack.deck import Deck


def twist(hand: Hand, deck: Deck) -> None:
    """Deals a card from the deck and adds it to the hand of cards

    Args:
        hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards
    """
    hand.add_card(deck.deal())


def stick_or_twist(hand: Hand, deck: Deck) -> None:
    """Asks for user input whether they would like to stick (not add any cards to their hand) or twist (add one card to their hand)

    Args:
        hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards

    Raises:
        Exception: Raises an exception if the user does not input a valid input of "s" or "t"
    """
    move = input("Stick or twist? Input s or t")
    while True:
        if move == "t":
            twist(hand, deck)
        elif move == "s":
            print("Player has chosen to stick.")
        else:
            raise Exception("Please enter either s or t")
        break


def reveal_cards(my_hand, reveal_all=True) -> None:
    """Reveal cards in the hand, printing the rank and value of the card

    Args:
        my_hand (_type_): Hand object representing a hand of cards
        reveal_all (bool, optional): If true, reveals all cards in the hand. If false, will only reveal one card in the hand. Defaults to True.
    """
    if reveal_all:
        for card in my_hand.cards:
            print(card)
    else:
        print(my_hand.cards[0])
