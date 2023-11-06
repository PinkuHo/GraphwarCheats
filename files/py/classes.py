# ============ Data Classes ============
class ConfigData:
    # ======== Declaring Variables ========
    # Ints
    enemyCounter = 0
    game_w, game_h = 50, 30  # total width and height of the game board in game coordinates

    # Screen points
    temp_point = None  # This is used to store a temporary point for the callback function

    left_top = [None]
    right_bottom = None

    # Graphwar points
    start_point = None
    enemy_points = []
