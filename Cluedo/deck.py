import random
import card

from card import Card

class Deck:

    def __init__(self):
        self.cards = []

        self.cards.append(Card("Dagger", card.WEAPON))
        self.cards.append(Card("Candlestick", card.WEAPON))
        self.cards.append(Card("Rope", card.WEAPON))
        self.cards.append(Card("Revolver", card.WEAPON))
        self.cards.append(Card("Lead Pipe", card.WEAPON))
        self.cards.append(Card("Spanner", card.WEAPON))
        
        self.cards.append(Card("Ballroom", card.ROOM))
        self.cards.append(Card("Hall", card.ROOM))
        self.cards.append(Card("Lounge", card.ROOM))
        self.cards.append(Card("Kitchen", card.ROOM))
        self.cards.append(Card("Conservatory", card.ROOM))
        self.cards.append(Card("Dining Room", card.ROOM))
        self.cards.append(Card("Library", card.ROOM))
        self.cards.append(Card("Study", card.ROOM))
        self.cards.append(Card("Billiard Room", card.ROOM))
        
        self.cards.append(Card("Miss Scarlet", card.PERSON)) 
        self.cards.append(Card("Professor Plumb", card.PERSON)) 
        self.cards.append(Card("Reverend Green", card.PERSON)) 
        self.cards.append(Card("Mrs. Peacock", card.PERSON)) 
        self.cards.append(Card("Colonel Mustard", card.PERSON)) 
        self.cards.append(Card("Mrs. White", card.PERSON)) 
    
    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def get_card_type(self, type):
        for card in self.cards:
            if card.card_type == type:
                return card

    def pop_card(self, i=-1):
        if len(self.cards) > 0:
            return self.cards.pop(i)
    
    def shuffle(self):
        random.shuffle(self.cards)

