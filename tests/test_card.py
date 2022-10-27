"""Tests the class Card, the associated methods and attributes"""
import pytest
from blackjack.card import Card


def test_card_string() -> None:
    """Tests the string output of a card object"""
    two_clubs = Card("Two", "Clubs")
    assert str(two_clubs) == "Two of Clubs"


def test_valid_rank() -> None:
    """Tests an assertion error is raised if rank is invalid"""
    with pytest.raises(AssertionError):
        Card("Test", "Two")


def test_valid_suit() -> None:
    """Tests an assertion error is raised if suit is invalid"""
    with pytest.raises(AssertionError):
        Card("Two", "Test")
