from blackjack.actions import reveal_cards
from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand


while True:
    print("Begin playing blackjack!")

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

    print("Dealer cards:")
    reveal_cards(dealer_hand, reveal_all=False)

    chips = Chips()
    chips.place_bet()

    break
