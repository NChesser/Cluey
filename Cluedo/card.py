ROOM = "Room"
WEAPON = "Weapon"
PERSON = "Person"

TYPES = (PERSON, WEAPON, ROOM)
class Card:

    def __init__(self, name, card_type):
        self.card_type = card_type
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.name, self.card_type))