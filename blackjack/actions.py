from blackjack.hand import Hand
from blackjack.deck import Deck
import config


def twist(hand: Hand, deck: Deck) -> None:
    """Deals a card from the deck and adds it to the hand of cards

    Args:
        hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards
    """
    hand.add_card(deck.deal())


def stick_or_twist(hand: Hand, deck: Deck) -> None:
    """Asks for user input whether they would like to stick (not add any cards to their hand)
    or twist (add one card to their hand)

    Args:
        hand (Hand): Hand object representing a hand of cards
        deck (Deck): Deck object representing a deck of cards

    Raises:
        Exception: Raises an exception if the user does not input a valid input of "s" or "t"
    """
    while True:
        move = input("Stick or twist? Input s or t: ")

        if move == "t":
            twist(hand, deck)
        elif move == "s":
            print("Player has chosen to stick.")
            config.playing = False
        else:
            raise Exception("Please enter either s or t")
        break


def reveal_cards(my_hand: Hand, reveal_all=True) -> None:
    """Reveal cards in the hand, printing the rank and value of the card

    Args:
        my_hand (Hand): Hand object representing a hand of cards
        reveal_all (bool, optional): If true, reveals all cards in the hand.
                                     If false, will only reveal one card in the hand.
                                     Defaults to True.
    """

    if reveal_all:
        for card in my_hand.cards:
            print(str(card))
    else:
        print(str(my_hand.cards[0]))


def continue_playing() -> None:
    """Ask player if they want to continue playing (input y or n)

    Raises:
        Exception: Exception raised when user has entered something other than y or n.
    """
    while True:
        play = input("Play again? Input y or n: ")
        if play == "y":
            config.playing = True
        elif play == "n":
            config.game_on = False
            break
        else:
            raise Exception("Please enter either y or n")
        break
