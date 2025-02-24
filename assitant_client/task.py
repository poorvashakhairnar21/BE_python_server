import time
import winsound
import threading
import os
import pyautogui
# from PIL import Image
# import cv2
from datetime import datetime
from speedtest import Speedtest
import subprocess
import platform
import time

from assitant_client.utils import APP_PATHS, SYSTEM_CONTROL_COMMANDS  

#done
def set_alarm(alarm_time:str):
    """Function to set an alarm on a separate thread."""
    def alarm_task(hour,minute):
        while True:
            now = datetime.now()
            if now.hour == hour and now.minute == minute:
                print("⏰ Alarm ringing!")
                for _ in range(5):  # Beeps 5 times
                    winsound.Beep(1000, 1000)
                break
            time.sleep(30)  # Check every 30 seconds
            
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        alarm_thread = threading.Thread(target=alarm_task,args=(alarm_hour,alarm_minute))
        alarm_thread.start()
        return(f"Alarm set for {alarm_time}.")
    except ValueError:
        return "Invalid format! Use HH:MM (24-hour). Try again."

#done
def open_application(app_name:str):
    """Function to open an application based on user command."""
    try:
        if app_name in APP_PATHS:
            subprocess.Popen(APP_PATHS[app_name], shell=True)  # No blocking, runs in the background
            return f"Opening {app_name}..."
        else:   
            return f"Application '{app_name}' not found!"
    except Exception as e:
        return f"Facing some issues while opening {app_name}."

#done
def take_screenshot():
    # Define the fixed folder name
    try:
        folder_path = "screenshots"
        
        # Create the "screenshots" folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Generate a unique filename using timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(folder_path, f"screenshot_{timestamp}.png")

    # Capture and save the screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        return f"Screenshot saved as {filename}"
    except Exception as e:
        return f"Facing some issues while taking screenshot."

# def take_photo():
#     # Create "photos" folder if it doesn't exist
#     folder_name = "photos"
#     os.makedirs(folder_name, exist_ok=True)

#     # Notify user and wait for 3 seconds
#     print("Get ready! Capturing photo in 3 seconds...")
#     time.sleep(3)  # Pause for 3 seconds

#     # Generate a unique filename using timestamp
#     timestamp = datetime.now().strftime("%Y-%m-%d")
#     filename = os.path.join(folder_name, f"img_{timestamp}.jpg")

#     # Open webcam
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print("Error: Could not open webcam")
#         return

#     # Capture photo
#     ret, frame = cam.read()
#     if ret:
#         cv2.imwrite(filename, frame)
#         print(f"Photo saved as {filename}")
#     else:
#         print("Failed to capture image")

#     cam.release()
#     cv2.destroyAllWindows()


#done
def get_internet_speed():
    try:
        st = Speedtest(timeout=1)
        download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps
        return f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps"
    except Exception as e:
        return f"Facing some issues while checking internet speed."

#done
def get_current_time():
    try:
        current_time = datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
        return f"The current time is {current_time}"
    except Exception as e:
        return f"Facing some issues while checking current time."

#halfdone
def system_control(command):
    # Validate action
    if command not in ["shutdown", "sleep", "restart"]:
        return "Invalid action. Please choose 'shutdown', 'sleep', or 'restart'."
    
    print(f"Are you sure you want to {command} the system? (yes/no): ", end="")
    choice = input().lower()

    if choice == "yes":
        print(f"Proceeding with {command}...")
        time.sleep(2)  # Add delay to give user time to read

        system_name = platform.system()

        if system_name in SYSTEM_CONTROL_COMMANDS  and command in SYSTEM_CONTROL_COMMANDS [system_name]:
            os.system(SYSTEM_CONTROL_COMMANDS [system_name][command])

    elif choice == "no":
        print("Action cancelled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")



'''

def open_spotify():
    """
    Opens the Spotify application.
    """
    try:
        subprocess.Popen("spotify", shell=True)
        time.sleep(5)  # Wait for Spotify to open
    except FileNotFoundError:
        print("Spotify not found! Ensure it's installed and in PATH.")

def play_song(song_name):
    """
    Searches and plays a song in Spotify.
    """
    try:
        open_spotify()  # Open Spotify if not already running

        # Open search bar in Spotify (Ctrl + L for Windows/Linux, Cmd + L for macOS)
        pyautogui.hotkey("ctrl", "k")  
        time.sleep(1)

        # Type the song name
        pyautogui.write(song_name)
        time.sleep(1)

        # Press 'Enter' to search
        pyautogui.press("enter")
        time.sleep(1)  # Wait for search results

        # Press 'Enter' to select and play the first result
        pyautogui.press("enter")
        print(f"Playing: {song_name}")

    except Exception as e:
        print("Error:", e)

def control_spotify(command):
    """
    Controls Spotify playback using media keys.
    """
    if command == "pause":
        pyautogui.press("playpause")
    elif command == "next":
        pyautogui.press("nexttrack")
    elif command == "previous":
        pyautogui.press("prevtrack")
    elif command == "volume up":
        pyautogui.press("volumeup")
    elif command == "volume down":
        pyautogui.press("volumedown")
    else:
        print("Unknown command!")


def close_spotify():
    """
    Closes Spotify application.
    """
    try:
        if platform.system() == "Windows":
            os.system("taskkill /F /IM Spotify.exe")  # Windows command to close Spotify
        else:
            os.system("pkill spotify")  # macOS/Linux command
        print("Spotify closed successfully.")
    except Exception as e:
        print("Error closing Spotify:", e)



# def open_spotify():
'''