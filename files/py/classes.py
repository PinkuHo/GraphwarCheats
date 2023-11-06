# ============ Data Classes ============
class ConfigData:
    # ======== Declaring Variables ========
    # Ints
    enemyCounter = 0
    game_top_left = (-25, 15)
    game_bottom_right = (25, -15)

    # Screen points
    temp_point = None  # This is used to store a temporary point for the callback function

    left_top = [None]
    right_bottom = None

    # Graphwar points
    start_point = None
    enemy_points = []
