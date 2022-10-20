from methods.deck import *
import random
import pytest

@pytest.fixture
def card_deck() -> Deck:
    return Deck()

def test_deck_string(card_deck: Deck):
    assert str(card_deck) == "Deck of 52 cards"
    
def test_shuffle(card_deck: Deck):
    shuffled_cards = random.shuffle(card_deck)
    assert card_deck.shuffle() == shuffled_cards # won't work yet because shuffle will be random. Need to add seed to compare.

def test_deal(card_deck: Deck):
    dealt_cards = card_deck.pop(2)
    assert dealt_cards == card_deck.deal()