import pytest
from blackjack.deck import Deck


@pytest.fixture
def card_deck() -> Deck:
    return Deck()


def test_deck_string(card_deck: Deck):
    assert str(card_deck) == "Deck of 52 cards"


def test_shuffle(card_deck: Deck):
    # todo
    pass


def test_deal(card_deck: Deck):
    dealt_cards = card_deck.pop(2)
    assert dealt_cards == card_deck.deal()
