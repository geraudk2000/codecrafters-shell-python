import sys


def main():
    # Uncomment this block to pass the first stage
    
    list_commands = set(["echo", "type", "exit"])

    # Wait for user input

    while True: 
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input()
        command = user_input.split(" ")[0]
        args = user_input.split(" ")[1:]
        if user_input == "exit 0":
            break
        elif command == "echo":
            sys.stdout.write(" ".join(args))
            sys.stdout.write("\n")
        elif command == "type": 
            cmd = args[0]
            if cmd in list_commands:
                sys.stdout.write(f"{cmd} is a shell builtin" )
                sys.stdout.write("\n")
            else: 
                sys.stdout.write(f"{cmd}: not found" )
                sys.stdout.write("\n")
        elif command not in list_commands:
            sys.stdout.write(f"{command}: command not found\n")
    

if __name__ == "__main__":
    main()
