'''
Main Game Function is a wrapper for making changes to the Inis game class
Handling Turn Events and exiting when a winner is found
'''

def main(inis):
    #setup
    #probably could easily be streamlined

    while winner == None:
        play_inis_turn()
    return inis.winner.name


def inis_turn():
    if inis.check_for_victory():
        return inis.winner

    inis.assign_bren()
    inis.assign_advantage_cards()
    inis.flip_crows_token()
    inis.resolve_tiles_actions()
   
    inis.draft()

    inis.seasons()
    # needs to stop on each season to make sure each player has the opportunity to play a triskel card
    return


def draft_phase():

    #deal cards
    for hand in inis.action_cards.deal_cards()
        players[i].hand = hand

    for i in range(3,1):
        #prompt response from each player

        #pass on the cards in the direction of the crows token

    return


def seasons_phase():

    all_pass = False:
    while all_pass = False:
        '''
        I almost want a function to update all chieftans and everything so all new info is available to AI
        every time anything happens
        '''
        inis.update()


        #step 1 - Make sure every player agent is aware of the victory conditions met by each player each turn
        inis.check_victory_conditions()

        #step 2 -



    pass

#use deepcopy to pass the game object to any players to allow decision making from current game state
#they have access to all the functions...

'''
Do i need some form of action validation to make sure no AI is cheating??
'''

if __name__ == "__main__":
    #TESTS