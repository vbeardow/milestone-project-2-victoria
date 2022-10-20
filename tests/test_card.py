from blackjack.card import *


def test_card_string():
    two_clubs = Card("Two", "Clubs")
    assert str(two_clubs) == "Two of Clubs"
