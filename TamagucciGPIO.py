from gpiozero import Button
from pynput.keyboard import Key, Controller
import time

BTN_LEFT = 17
BTN_RIGHT = 27
BTN_SPACE = 4
BTN_ESCAPE = 5

# Create a keyboard controller object
keyboard = Controller()


def main():
    try:
        
        left_down = False
        right_down = False
        space_down = False
        escape_down = False

        
        left = Button(BTN_LEFT)
        right = Button(BTN_RIGHT)
        space = Button(BTN_SPACE)
        escape = Button(BTN_ESCAPE)

        press_count = 0
        release_count = 0

        debounce_time = 0.25
        press_time = time.time()

        while True:

            if(time.time() - press_time < debounce_time):
                continue

            if left.is_pressed:
                if not left_down:
                    left_down = True
                    press_time = time.time()
                    press_count+=1
                    keyboard.press(Key.left)
                    print("Left pressed %d" % press_count)
            else:
                if left_down:
                    left_down = False
                    press_time = time.time()
                    release_count+=1
                    keyboard.release(Key.left)
                    print("Left released %d" % release_count)

            if right.is_pressed:
                if not right_down:
                    right_down = True
                    press_time = time.time()
                    press_count+=1
                    keyboard.press(Key.right)
                    print("Right pressed %d" % press_count)
            else:
                if right_down:
                    right_down = False
                    press_time = time.time()
                    release_count+=1
                    keyboard.release(Key.right)
                    print("Right released %d" % release_count)

            if space.is_pressed:
                if not space_down:
                    space_down = True
                    press_time = time.time()
                    press_count+=1
                    keyboard.press(Key.space)
                    print("Space pressed %d" % press_count)
            else:
                if space_down:
                    space_down = False
                    press_time = time.time()
                    release_count+=1
                    keyboard.release(Key.space)
                    print("Space released %d" % release_count)

            if escape.is_pressed:
                if not escape_down:
                    escape_down = True
                    press_time = time.time()
                    press_count+=1
                    keyboard.press(Key.esc)
                    print("Escape pressed %d" % press_count)
            else:
                if escape_down:
                    escape_down = False
                    press_time = time.time()
                    release_count+=1
                    keyboard.release(Key.esc)
                    print("Escape released %d" % release_count)

    except KeyboardInterrupt:
        print("\nExiting program...")

if __name__ == "__main__":
    main()
