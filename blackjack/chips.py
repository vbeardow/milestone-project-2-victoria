"""Defines the class "Chips" which represents a players betting chips"""
import blackjack.game_config as game_config


class Chips:
    """A class representing a players betting chips"""

    def __init__(self) -> None:
        """Set the attributes of chips total to 100 and bet to 0.
        Do not allow bets higher than the total chips."""
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
                elif self.bet < 0:
                    print("You can not place a negative bet, please try again.")
                else:
                    break

    def no_chips_remaining(self) -> bool:
        """If no chips remaining, print statement to player and end game.

        Returns:
            bool: Returns true if there are no chips remaining. Returns false otherwise.
        """
        if self.total == 0:
            print("You have no chips left! Game over.")
            game_config.game_on = False
            return True
        else:
            return False
