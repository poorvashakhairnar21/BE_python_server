from assitant_client.commands import COMMANDS

def main():
    while True:
        command = input("Enter command: ").strip().lower()
        
        command_execute = COMMANDS.get(command,"")
        
        if command_execute:
            command_execute()
            
        # elif command.startswith("open "):  
        #     open_application(command)  # Extracts app name & opens it

        # elif "action" in command:
        #     action = input("Enter action (shutdown/sleep/restart): ").lower()
        #     system_control(action)

        # elif command.startswith("play "):
        #     song_name = command[5:]  # Extract song name
        #     play_song(song_name)

        # elif command == "pause":
        #     control_spotify("pause")

        # elif command == "next":
        #     control_spotify("next")

        # elif command == "previous":
        #     control_spotify("previous")

        # elif command == "volume up":
        #     control_spotify("volume up")

        # elif command == "volume down":
        #     control_spotify("volume down")

        # elif command =="close spotify":
        #     print("closing spotify in 1...")
        #     time.sleep(1)
        #     close_spotify()

        # elif command == "exit":
        #     print("Exiting...")
        #     break
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
