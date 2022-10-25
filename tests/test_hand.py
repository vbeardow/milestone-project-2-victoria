"""Tests the class Hand, the associated methods and attributes"""


from blackjack.card import Card
from blackjack.hand import Hand


def test_add_card(player_hand: Hand):
    """Tests the size and value of the hand are correct after adding a card

    Args:
        player_hand (Hand): Empty hand of cards
    """
    player_hand.add_card(Card("Two", "Hearts"))
    assert len(player_hand.cards) == 1
    assert player_hand.value == 2


def test_add_ace(player_hand: Hand):
    """Tests that the ace count is correct after adding an ace

    Args:
        player_hand (Hand): Empty hand of cards
    """
    new_card = Card("Ace", "Clubs")
    player_hand.add_card(new_card)
    assert player_hand.aces == 1


def test_value_with_ace(player_hand: Hand):
    """Tests that the value of cards is adjusted if the total value is above 21 and the hand includes at an ace

    Args:
        player_hand (Hand): Empty hand of cards
    """
    player_hand.aces = 1
    player_hand.value = 22
    player_hand.adjust_for_ace()
    assert player_hand.value == 12
    assert player_hand.aces == 0
