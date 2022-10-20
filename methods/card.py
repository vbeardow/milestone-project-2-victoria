class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'