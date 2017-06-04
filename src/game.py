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
    def __init__(self):
        self.deck = [i for i in range(1,14) for j in range(0,4)]
        shuffle(self.deck)
        self.p1_start = self.deck[:26]
        self.p2_start = self.deck[26:]
        self.player_1 = Player(self.p1_start, "Player 1")
        self.player_2 = Player(self.p2_start, "Player 2")
        self.winner = None
        self.num_turns = 0
    def war(self, pot, extra_cards):
        pot += [self.player_1.get_next_card() for i in range(0,extra_cards)] +
        [self.player_2.get_next_card() for i in range(0,extra_cards)]
        card_1 = self.player_1.get_next_card()
        card_2 = self.player_2.get_next_card()
        if card_1 == None:
            self.winner = 0
            return()
        elif card_2 == None:
            self.winner = 1
            return()
        pot += [card_1, card_2]
        if card_1 > card_2:
            self.player_1.add_winnings(pot)
        elif card_1 < card_2:
            self.player_2.add_winnings(pot)
        elif card_1 == card_2:
            self.war(pot, 2)
    def play(self):
        while self.winner == None:
            card_1 = self.player_1.get_next_card()
            card_2 = self.player_2.get_next_card()
            if card_1 == None:
                self.winner = 0
                break
            elif card_2 == None:
                self.winner = 1
                break
            self.num_turns += 1
            if card_1 > card_2:
                self.player_1.add_winnings([card_1, card_2])
            elif card_1 < card_2:
                self.player_2.add_winnings([card_1, card_2])
            elif card_1 == card_2:
                self.war([card_1, card_2])

g = [Game() for i in range(0,10000)]
