"""Defines the class "Chips" which represents a players betting chips"""


class Chips:
    """A class representing a players betting chips"""

    def __init__(self):
        """Set the attributes of chips total to 100 and bet to 0. Do not allow bets higher than the total chips."""
        self.total = 100
        self.bet = 0

    def win_bet(self) -> None:
        """Increase the chips total by the bet value if the bet is won"""
        self.total += self.bet

    def lose_bet(self) -> None:
        """Decrease the chips total by the bet value if the bet is lost"""
        self.total -= self.bet

    def place_bet(self) -> None:
        """Takes a user input for to place the bet

        Raises:
            ValueError: Input bet is not an integer
        """
        while True:
            try:
                self.bet = int(input("Place your bet: "))
            except ValueError:
                print("Please enter an integer")
            else:
                if self.bet > self.total:
                    print(
                        f"You can not place a bet higher than your current total of {self.total}."
                    )
                else:
                    break
