# ============ Imports ============
# Python
import time


# ============ Functions ============
class Functions:
    # -- Window points --
    @staticmethod
    def select_point_callback(x, y, button, pressed):
        # ======== Imports ========
        # Internal
        from files.py.classes import ConfigData
        # Packages
        from pynput import mouse

        # ======== Start of Code ========

        # If the left mouse button is pressed, store the selected point
        if button == mouse.Button.left and pressed:
            ConfigData.temp_point = [x, y]

    @staticmethod
    def select_point():
        # ======== Imports ========
        # Packages
        from pynput import mouse

        # Internal
        from files.py.classes import ConfigData

        # ======== Declaring Variables ========
        ConfigData.temp_point = None

        # ======== Start of Code ========
        # Create a listener for mouse clicks
        listener = mouse.Listener(
            on_click=lambda x, y, button, pressed: Functions.select_point_callback(x, y, button, pressed))
        listener.start()

        # Wait for the user to click the mouse
        while ConfigData.temp_point is None:
            time.sleep(1)

        # Stop the listener
        listener.stop()
        # Return the selected point
        return ConfigData.temp_point

    @staticmethod
    def getWindowPoints():
        # ======== Imports ========
        # Internal
        from files.py.classes import ConfigData

        # Packages
        from tkinter import messagebox

        # ======== Start of Code ========
        # Printing the start message
        messagebox.showinfo("Select Game Axes",
                            "Press OK and left click on the top left and then the bottom right corners of the game "
                            "axes.")

        # Getting the left top point
        ConfigData.left_top = Functions.select_point()
        print("Left top point made")
        ConfigData.right_bottom = Functions.select_point()
        print("Right bottom point made")

    # -- Graphwar --
    @staticmethod
    def normalize_point(x, y):
        # ======== Imports ========
        # Internal
        from files.py.classes import ConfigData

        # ======== Start of Code ========
        game_width = ConfigData.game_bottom_right[0] - ConfigData.game_top_left[0]
        game_height = ConfigData.game_top_left[1] - ConfigData.game_bottom_right[1]

        normalized_x = ((x - ConfigData.left_top[0]) / (
                ConfigData.right_bottom[0] - ConfigData.left_top[0])) * game_width + ConfigData.game_top_left[0]

        # Invert the y-coordinate by subtracting from the top-left y-coordinate
        # and then inverting the direction since screen coordinates increase downwards
        normalized_y = ConfigData.game_top_left[1] - (((y - ConfigData.left_top[1]) / (
                ConfigData.right_bottom[1] - ConfigData.left_top[1])) * game_height)

        return normalized_x, normalized_y

    @staticmethod
    def getGraphwarPoints():
        # ======== Imports ========
        # Internal
        from files.py.classes import ConfigData

        # Packages
        from tkinter import messagebox
        import keyboard

        # ======== Declaring Variables ========
        counter = 0

        # ======== Start of Code ========
        # Printing the start message
        messagebox.showinfo("Game Start",
                            "Press OK and left click your character and then select the other players. Hit escape and "
                            "click to select the last player.")

        # Getting the start point and normalizing it
        ConfigData.start_point = Functions.select_point()
        ConfigData.start_point = Functions.normalize_point(ConfigData.start_point[0], ConfigData.start_point[1])
        print(f"Start point made: {ConfigData.start_point}")

        # Get the enemy path points
        while not keyboard.is_pressed("esc"):
            # ==== Declaring Variables ====
            # Points
            next_point = Functions.select_point()
            next_point = Functions.normalize_point(next_point[0], next_point[1])

            # ==== Start of Code ====
            # Adding the point to the list
            ConfigData.enemy_points.append(next_point)
            print(f"Enemy point {counter} made: {next_point}")
            counter += 1

    @staticmethod
    def calculate_formula_graphwar(point_list):
        start = point_list[0]
        x1, y1 = start[0], start[1]
        result = ""

        for point in point_list[1:]:
            x2, y2 = point[0], point[1] - y1
            result += "+" + str(y2) + "*((x+" + str(x2) + ")/(abs(x+" + str(x2) + ")+0.01))"
            x1, y1 = x2, y2
        result = "0.5*(" + result[1:] + ")"
        result = result.replace("+-", "-")
        return result

    # -- Start --
    @staticmethod
    def startGraphWarCheats():
        # ======== Imports ========
        # Internal
        from files.py.classes import ConfigData

        # ======== Declaring Variables ========
        # Window points
        Functions.getWindowPoints()

        # Graphwar points
        Functions.getGraphwarPoints()

        # ======== Start of Code ========
        # Making the formula to hit the enemies
        print("Making formula")
        result = Functions.calculate_formula_graphwar(ConfigData.enemy_points)

        # Printing the result
        print(result)
