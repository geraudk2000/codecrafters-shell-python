import sys


def main():
    # Uncomment this block to pass the first stage
    
    list_commands = set("echo")
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
        elif command not in list_commands:
            sys.stdout.write(f"{command}: command not found\n")
    

if __name__ == "__main__":
    main()
