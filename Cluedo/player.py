import random
from collections import defaultdict
from collections import Counter
import itertools

import card
from deck import Deck

class Player:

    def __init__(self, name, number_other_players):
        self.name = name
        self.hand = []
        self.deck = Deck()
        self.deck.shuffle()
        self.players_dict = defaultdict(list)
        self.number_other_players = number_other_players

    def add_card(self, card):
        self.hand.append(card)
        self.deck.remove_card(card)

    def add_known_cards(self, card_counts):
        for card in card_counts:
            if card_counts[card] == self.number_other_players:
                self.deck.cards = [c for c in self.deck.cards if card.card_type != c.card_type or c.name == card.name]

    def add_suggestion_card(self, type):
        #Checks cards unknown by other players

        known = [c for c in self.players_dict.values()]  
        c = Counter(list(itertools.chain.from_iterable(known)))

        self.add_known_cards(c)
        
        return self.deck.get_card_type(type)
        

    def make_suggestion(self):
        suggestion = [self.add_suggestion_card(t) for t in card.TYPES]

        print (self.name + " Suggesting")
        print (suggestion)

        return suggestion

    def show(self, player, card):        
        if card in self.hand:
            player.deck.remove_card(card)
            return True
        
        return False

    def add_unknown_cards(self, player, cards):  
        for c in cards:
            if c not in self.players_dict[player.name]:
                self.players_dict[player.name].append(c)

    def guess_shown_card(self, player, cards):        
        my_list = [c for c in cards if c not in self.players_dict[player.name]]
        if len(my_list) == 1:
            self.deck.remove_card(my_list.pop())




        
        


        