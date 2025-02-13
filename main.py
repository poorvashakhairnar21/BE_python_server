from assitant_client.commands import COMMANDS

command = "time"
parameters = {}
def main():
    command_execute, _ = COMMANDS.get(command,"")
    
    if command_execute:
        print(command_execute(**parameters))

if __name__ == "__main__":
    main()
