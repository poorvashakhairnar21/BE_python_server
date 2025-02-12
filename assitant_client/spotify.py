import subprocess
import pyautogui
import time

def execute_command(command):
    """
    Takes a command like 'play song_name' and plays the song on Spotify.
    """
    if command.lower().startswith("play "):
        song_name = command[4:]  # Extract the song name after 'play '
        play_song(song_name)
    else:
        print("Invalid command! Use 'play <song_name>'")

def play_song(song_name):
    """
    Opens Spotify, searches for the song, and plays it.
    """
    try:
        # Open Spotify
        subprocess.Popen("spotify", shell=True)
        time.sleep(5)  # Wait for Spotify to open

        # Open search bar in Spotify (Ctrl + L for Windows/Linux, Cmd + L for macOS)
        pyautogui.hotkey("ctrl", "l")  
        time.sleep(1)

        # Type the song name
        pyautogui.write(song_name, interval=0.1)
        time.sleep(1)

        # Press 'Enter' to search
        pyautogui.press("enter")
        time.sleep(2)  # Wait for search results

        # Press 'Enter' to select and play the first result
        pyautogui.press("enter")
        print(f"Playing: {song_name}")

    except Exception as e:
        print("Error:", e)

# Example Usage
command = input("Enter your command: ")
execute_command(command)
