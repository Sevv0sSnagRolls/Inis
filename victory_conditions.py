"""


"""

class victory_conditions():
    """
    Hold information about each victory condition for each player
    """
    def __init__(self, player_id, condition):
        self.player_id = player_id
        self.condition = condition
        self.victory = False
        self.qty = 0
        self.positions = []

    def update_victory_conditions(self, victory_bool, qty, positions):
        self.victory = victory_bool
        self.qty = qty
        self.positions = positions