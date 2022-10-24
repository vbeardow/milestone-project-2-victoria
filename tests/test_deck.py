import pytest
from blackjack.deck import Deck


def test_deck_size(card_deck: Deck):
    """Tests the number of cards in the deck is 52"""
    assert len(card_deck.deck) == 52


def test_deck_string(card_deck: Deck):
    """Tests the string of first and last cards in an ordered deck

    Args:
        card_deck (Deck): An ordered deck of 52 cards
    """
    card_list = str(card_deck).split("\n")[:-1]
    assert card_list[0] == "Two of Hearts"
    assert card_list[-1] == "Ace of Clubs"


def test_shuffle(card_deck: Deck):
    """Tests that the order of cards in the deck is not equal to the
    order of cards after the deck has been shuffled

    Args:
        card_deck (Deck): An ordered deck of 52 cards
    """
    ordered_deck = Deck()
    card_deck.shuffle()
    assert str(ordered_deck) != str(card_deck)


def test_deal(card_deck: Deck):
    """Tests a single card dealt from the deck

    Args:
        card_deck (Deck): An ordered deck of 52 cards
    """
    new_deck = Deck()
    expected_cards = new_deck.deck.pop()
    dealt_cards = str(card_deck.deal())
    assert dealt_cards == str(expected_cards)
