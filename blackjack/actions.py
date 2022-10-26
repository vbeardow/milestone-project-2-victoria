"""Defines game actions for the game blackjack"""

from typing import List
from blackjack.hand import Hand
from blackjack.deck import Deck
import blackjack.game_config as game_config


def print_invalid_input(options: List[str]) -> None:
    """Print invalid input statement

    Args:
        options (List[str]): list of valid input options
    """
    print(f"Invalid input. Please enter one of the following options: {options}.")


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

    """
    while True:
        move = input("Stick or twist? Input s or t: ")

        if move.lower() == "t":
            twist(hand, deck)
        elif move.lower() == "s":
            print("Player has chosen to stick.")
            game_config.playing = False
        else:
            print_invalid_input(["s", "t"])
        break


def dealer_twist(hand: Hand, deck: Deck) -> None:
    """Deal cards to the dealer up to a total hand value of 17

    Args:
        hand (Hand): Hand object representing the dealer's cards
        deck (Deck): _description_
    """
    while hand.value <= 17:
        twist(hand, deck)


def reveal_cards(hand: Hand, reveal_all: bool = True) -> None:
    """Reveal cards in the hand, printing the rank and value of the card

    Args:
        player_hand (Hand): Hand object representing a hand of cards
        reveal_all (bool, optional): If true, reveals all cards in the hand.
                                     If false, will only reveal one card in the hand.
                                     Defaults to True.
    """

    if reveal_all:
        for card in hand.cards:
            print(str(card))
    else:
        print(str(hand.cards[0]))


def continue_playing() -> None:
    """Ask player if they want to continue playing (input y or n)"""
    while True:
        play = input("Keep playing? Input y or n: ")

        if play.lower() == "y":
            game_config.playing = True
            break
        elif play.lower() == "n":
            game_config.game_on = False
            break
        else:
            print_invalid_input(["y", "n"])
