import pyautogui
import random
import time


def move_mouse_randomly():
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    while True:
        # Generate random x and y coordinates within the screen bounds
        random_x = random.randint(0, screen_width - 1)
        random_y = random.randint(0, screen_height - 1)

        # Move the mouse to the random position
        pyautogui.moveTo(random_x, random_y)
        print(f"Mouse moved to: ({random_x}, {random_y})")

        # Wait for 1 hour (3600 seconds)
        time.sleep(30)


if __name__ == "__main__":
    move_mouse_randomly()
