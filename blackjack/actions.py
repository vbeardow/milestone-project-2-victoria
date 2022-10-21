from blackjack.hand import Hand
from blackjack.deck import Deck


def twist(hand: Hand, deck: Deck):
    hand.add_card(deck.deal())


def stick_or_twist(hand: Hand, deck: Deck):
    move = input("Stick or twist? Input s or t")
    while True:
        if move == "t":
            twist(hand, deck)
        elif move == "s":
            print("Player has chosen to stick.")
        else:
            raise Exception("Please enter either s or t")
        break
