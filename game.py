from blackjack.actions import reveal_cards, stick_or_twist
from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand
import config

while True:

    print("Begin blackjack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    print("Players cards:")
    reveal_cards(player_hand, reveal_all=True)
    # print("Player value total:", player_hand.value)

    print("Dealer cards:")
    reveal_cards(dealer_hand, reveal_all=False)

    chips = Chips()
    chips.place_bet()

    while config.playing:
        stick_or_twist(player_hand, deck)
        print("Player value total:", player_hand.value)

        if player_hand.value >= 21:
            config.playing = False
        else:
            continue
    break
