import pytest
from blackjack.card import Card
from blackjack.hand import Hand


@pytest.fixture
def my_hand() -> Hand:
    return Hand()


def test_add_card(my_hand: Hand):
    my_hand.add_card(Card("Two", "Hearts"))
    assert len(my_hand.cards) == 1
    assert my_hand.value == 2


def test_add_ace(my_hand: Hand):
    new_card = Card("Ace", "Clubs")
    my_hand.add_card(new_card)
    assert my_hand.aces == 1


def test_value_with_ace(my_hand: Hand):
    my_hand.aces = 1
    my_hand.value = 22
    my_hand.adjust_for_ace()
    assert my_hand.value == 12
    assert my_hand.aces == 0
