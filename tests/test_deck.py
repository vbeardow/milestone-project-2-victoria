import pytest
from blackjack.deck import Deck


@pytest.fixture
def card_deck() -> Deck:
    return Deck()


def test_deck(card_deck: Deck):
    assert len(card_deck.deck) == 52


def test_deck_string(card_deck: Deck):
    assert card_deck.__str__()[0] == "Two of Hearts"


def test_shuffle(card_deck: Deck):
    ordered_deck = Deck()
    card_deck.shuffle()
    assert ordered_deck.__str__() != card_deck.__str__()


def test_deal(card_deck: Deck):
    dealt_cards = card_deck.deck.pop(2)
    assert dealt_cards == card_deck.deal()
