from assitant_client.task import *

COMMANDS = {
    "set alarm": [set_alarm,{"time": ""}],
    # "take photo": [take_photo,{}],
    "screenshot": [take_screenshot,{}],
    "internet speed": [get_internet_speed,{}],
    "time": [get_current_time,{}],
    # "action": [system_control,{}], 
    "open": [open_application,{"app_name":""}],
    # Requires user input
    # "play": play_song,  # Requires extracted song name
    # "pause": lambda: control_spotify("pause"),
    # "next": lambda: control_spotify("next"),
    # "previous": lambda: control_spotify("previous"),
    # "volume up": lambda: control_spotify("volume up"),
    # "volume down": lambda: control_spotify("volume down"),
    # "close spotify": close_spotify,
    # "exit": exit,  # Can be handled separately
}




{'set alarm': {'time': ''},'take photo': {},'screenshot': {},'internet speed': {},'time': {},'action': {},'open': {'app_name': ''}}