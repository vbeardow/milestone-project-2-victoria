from blackjack.card import Card


def test_card_string() -> None:
    """Tests the string output of a card object"""
    two_clubs = Card("Two", "Clubs")
    assert str(two_clubs) == "Two of Clubs"
