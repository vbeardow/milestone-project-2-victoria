from methods.card import *

def test_card():
    two_clubs = Card("Two", "Clubs")
    assert str(two_clubs) == "Two of Clubs"