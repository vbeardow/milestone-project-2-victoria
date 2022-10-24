from blackjack.actions import continue_playing, reveal_cards, stick_or_twist
from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.results import determine_winner, player_bust
import config

player_chips = Chips()

while config.game_on:

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

    while config.playing:
        # Ask the player if they want to stick or twist
        stick_or_twist(player_hand, deck)
        print("Player value total:", player_hand.value)
        print(f"Player has {player_hand.aces} aces")

        # Exist play if the player is bust
        if player_hand.value > 21:
            player_bust(player_chips)
            config.playing = False
            break

    if player_hand.value <= 21:
        # Deal cards to the dealer up to a value of 17
        while dealer_hand.value <= 17:
            dealer_hand.add_card(deck.deal())

        print("Dealer value total:", dealer_hand.value)

        # Determine the winner
        determine_winner(player_hand, dealer_hand, player_chips)

    print(f"Player has a total of {player_chips.total} chips remaining")

    # Ask if player wants to continue play
    continue_playing()
