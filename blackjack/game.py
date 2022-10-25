"""
Compiles the modules for the game blackjack into a single game file. 

Run the command "make run" to play the game blackjack.
"""
from blackjack.actions import continue_playing, reveal_cards, stick_or_twist, twist
from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.results import determine_winner, player_bust
import blackjack.game_config as game_config


def play_game():
    """Function executes a game of blackjack"""

    player_chips = Chips()

    while game_config.game_on:

        print("Begin blackjack!")

        # Initialise the deck of cards and shuffle the deck
        deck = Deck()
        deck.shuffle()

        # Deal two cards from the deck to the players hand
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        # Deal two cards from the deck to the dealers hand
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Reveal both the players cards and total value
        print("Players cards:")
        reveal_cards(player_hand, reveal_all=True)
        print("Player value total:", player_hand.value)

        # Reveal one of the dealers cards
        print("Dealer cards:")
        reveal_cards(dealer_hand, reveal_all=False)

        # Ask the player for their bet
        player_chips.place_bet()

        while game_config.playing:
            # Ask the player if they want to stick or twist
            stick_or_twist(player_hand, deck)
            print("Player value total:", player_hand.value)

            # Exist play if the player is bust
            if player_hand.value > 21:
                player_bust(player_chips)
                break

        if player_hand.value <= 21:
            # Deal cards to the dealer up to a value of 17
            while dealer_hand.value <= 17:
                twist(dealer_hand, deck)

            print("Dealer value total:", dealer_hand.value)

            # Determine the winner
            determine_winner(player_hand, dealer_hand, player_chips)

        if player_chips.total == 0:
            print("You have no chips left! Game over.")
            game_config.game_on = False
        else:
            print(f"Player has a total of {player_chips.total} chips remaining")
            # Ask if player wants to continue play
            continue_playing()


if __name__ == "__main__":
    play_game()
