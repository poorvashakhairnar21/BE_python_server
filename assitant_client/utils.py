APP_PATHS = {
    "notepad": "notepad.exe",
    "spotify": "spotify.exe",
    "calculator": "calc.exe",
    "chrome": "chrome.exe",
    "vlc": "vlc.exe",
    "camera": "start microsoft.windows.camera:",
    "word": "winword",
    "excel": "EXCEL.EXE"
}

SYSTEM_CONTROL_COMMANDS = {
    "Windows": {
        "shutdown": "shutdown /s /t 1",
        "sleep": "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
        "restart": "shutdown /r /t 1"
    },
    "Darwin": {  # macOS
        "shutdown": "sudo shutdown -h now",
        "sleep": "pmset sleepnow",
        "restart": "sudo shutdown -r now"
    },
    "Linux": {
        "shutdown": "shutdown now",
        "sleep": "systemctl suspend",
        "restart": "reboot"
    }
}