from random import shuffle


class Player():
    """docstring for Player."""
    def __init__(self, hand, name):
        self.hand = hand[:]
        self.name = name
    def add_winnings(self, cards):
        shuffle(cards)
        self.hand += cards
    def get_next_card(self):
        if len(self.hand)==0:
            return(None)
        else:
            next_card = self.hand.pop(0)
            return(next_card)

class Game():
    """docstring for Game."""
    def __init__(self, war_anti):
        self.war_anti = war_anti
        self.deck = [i for i in range(1,14) for j in range(0,4)]
        shuffle(self.deck)
        self.p0_start = self.deck[:26]
        self.p1_start = self.deck[26:]
        self.player_0 = Player(self.p0_start, "Player 0")
        self.player_1 = Player(self.p1_start, "Player 1")
        self.winner = None
        self.num_turns = 0
    def war(self, pot, extra_cards):
        pot += [self.player_0.get_next_card() for i in range(0,extra_cards)] + [self.player_1.get_next_card() for i in range(0,extra_cards)]
        card_0 = self.player_0.get_next_card()
        card_1 = self.player_1.get_next_card()
        if card_0 == None:
            self.winner = 1
            return()
        elif card_1 == None:
            self.winner = 0
            return()
        pot += [card_0, card_1]
        if card_0 > card_1:
            self.player_0.add_winnings(pot)
        elif card_0 < card_1:
            self.player_1.add_winnings(pot)
        elif card_0 == card_1:
            self.war(pot, self.war_anti)
    def play(self):
        while self.winner == None:
            self.num_turns += 1
            self.war([], 0)
