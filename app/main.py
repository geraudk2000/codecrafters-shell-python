import sys
import os


def main():
    # Uncomment this block to pass the first stage
    
    list_commands = set(["echo", "type", "exit"])
    PATH = os.environ.get('PATH')
    # Wait for user input

    while True: 
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input()
        command = user_input.split(" ")[0]
        args = user_input.split(" ")[1:]
        paths = PATH.split(":")
        path_found = False
        
        if user_input == "exit 0":
            break
        elif command == "echo":
            sys.stdout.write(" ".join(args))
            sys.stdout.write("\n")
        elif command == "type": 
            cmd = args[0]
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    sys.stdout.write(f"{cmd} is {path}/{cmd}\n" )
                    path_found = True
            if not path_found:
                sys.stdout.write(f"{cmd}: command not found\n")

        elif command not in list_commands:
            sys.stdout.write(f"{command}: command not found\n")
    

if __name__ == "__main__":
    main()
