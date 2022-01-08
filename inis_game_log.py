"""
Idea is to have an object which is setup with good data structures for savins
- game states
- Drafting phase actions
- Season phase actions
etc

So basically can save to SQL or wtv with specific format
that means I can re render the gameplay in Javascript or some shit
or learn from what was played
etc etc #bsdatascience
"""

import pandas as pd

draft_phase_columns = ['round_number', 'player', 'cards_dealt', 'cards_kept', 'cards_passed']
draft_phase_columns = ['round_number', 'player', 'cards_dealt', 'cards_kept', 'cards_passed']
draft_phase_columns = ['round_number', 'player', 'cards_dealt', 'cards_kept', 'cards_passed']

class game_logger():

    def __init__(self):
        round_number = 0
        draft_phase_moves = []

