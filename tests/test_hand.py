from blackjack.card import Card
from blackjack.hand import *
import pytest


@pytest.fixture
def my_hand() -> Hand:
    return Hand()


@pytest.fixture
def new_card() -> Card:
    return Card("Ace", "Hearts")


def test_add_card(my_hand: Hand, new_card: Card):
    expected_hand = my_hand.append(new_card)
    assert my_hand.add_card(new_card) == expected_hand


def test_adjust_for_ace(my_hand: Hand, new_card: Card):
    my_hand.append(new_card)
    my_hand.adjust_for_ace()
    assert my_hand.aces == 1
