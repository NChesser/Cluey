import random
import card
from player import Player
from deck import Deck

class SetUp:        

    def __init__(self, number_of_players):         
        self.deck = Deck()
        self.deck.shuffle()
        self.crime = self.crime_setup() 
        self.deck.cards = [c for c in self.deck.cards if c not in self.crime]
        self.players = self.player_setup(number_of_players)

    def crime_setup(self):
        crime = [self.deck.get_card_type(t) for t in card.TYPES]

        print("Crime")
        print(crime)
        return crime

    def player_setup(self, number_of_players):
        player_list = [Player("Player " + str(player), number_of_players) for player in range (0, number_of_players)]
        
        #Give players cards
        while(len(self.deck.cards) > 0):
            for player in player_list:
                if len(self.deck.cards) > 0:
                    player.add_card(self.deck.pop_card())

        return player_list

        
