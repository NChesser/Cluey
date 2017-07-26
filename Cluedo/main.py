from setup import SetUp

#Cluedo Game
    
def game(times=100):
    #adding a comment here to test
    rounds = 0
    for i in range(0, times):        
        new_game = SetUp(6)
        rounds += handle_turns(new_game.players, new_game.crime)

    print ("Average rounds taken " + str(rounds/times))

def handle_turns(players, crime):
    found = False
    count = 0

    while not found:
        guesser = players.pop(0)        
        found =handle_suggestion(guesser, players, guesser.make_suggestion())
        count += 1
        players.append(guesser)        
    
    print ("The Crime was commited in the " + crime[2].name + " by " + crime[0].name + " with the " + crime[1].name) 
    print ("Rounds to solve " + str(count/len(players))) 

    return count/len(players)  
      

def handle_suggestion(player, players, cards):
    for p in players:
        for c in cards: 
            if p.show(player, c):
                guess_shown_card(players, p, cards)                  
                return False
        add_unknown_cards(players, p, cards)                                    

    print (player.name + " Wins")
    return True

#Player analysis after suggestions
def guess_shown_card(players, player, cards):
    for p in players:        
        p.guess_shown_card(player, cards)

def add_unknown_cards(players, player, cards):
    for p in players:
        p.add_unknown_cards(player, cards)

if __name__ == "__main__":
    game()
