import pytest
from blackjack.chips import Chips
from unittest.mock import patch


@pytest.fixture
def chips():
    """Create chips class for testing

    Returns:
        _type_: an instance of a class of chips
    """
    return Chips()


def test_win_bet(chips: Chips):
    """Test the chips total increases if bet is won

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.win_bet()
    assert chips.total == 100 + 10


def test_lose_bet(chips: Chips):
    """_summary_

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.bet = 10
    chips.lose_bet()
    assert chips.total == 100 - 10


@patch("builtins.input", lambda *args: 12)
def test_place_bet(chips: Chips):
    """Tests that if the function place_bet is called, the property bet of the chips is equal to the user input

    Args:
        chips (Chips): A chips class with a total of 100
    """
    chips.place_bet()
    assert chips.bet == 12


@patch("builtins.input", lambda *args: "twelve")
def test_place_bet_non_integer(chips: Chips):
    """Tests that a value error is thrown if the bet the user inputs is not an integer value

    Args:
        chips (Chips): A chips class with a total of 100
    """
    with pytest.raises(ValueError, match="Please enter an integer"):
        chips.place_bet()


@patch("builtins.input", lambda *args: 110)
def test_place_bet_exceeds_total(chips: Chips):
    """Tests that an exception is thrown if the bet the user inputs exceeds the total

    Args:
        chips (Chips): A chips class with a total of 100
    """
    with pytest.raises(
        Exception, match="You can not place a bet higher than your current total."
    ):
        chips.place_bet()
