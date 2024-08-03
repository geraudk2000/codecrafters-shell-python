import sys
import os


def main():
    # Uncomment this block to pass the first stage
    
    list_commands = set(["echo", "type", "exit", "pwd", "cd"])
    PATH = os.environ.get('PATH')
    # Wait for user input

    while True: 
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input()
        command = user_input.split(" ")[0]
        args = user_input.split(" ")[1:]
        paths = PATH.split(":")

        if len(user_input.split(" "))>1:
            cmd = args[0]
        
        if user_input == "exit 0":
            break
        elif command == "echo":
            sys.stdout.write(" ".join(args))
            sys.stdout.write("\n")
        elif command == "type": 
            
            if cmd and cmd in list_commands: 
                sys.stdout.write(f"{cmd} is a shell builtin\n" )
                continue
            elif cmd:
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        sys.stdout.write(f"{cmd} is {path}/{cmd}\n" )
                        break
                else:
                    sys.stdout.write(f"{cmd}: not found\n")
        elif command == "pwd": 
            sys.stdout.write(os.getcwd() + "\n")
        elif command == "cd":
            if cmd: 
                try:
                    os.chdir(cmd)
                    continue
                except Exception as e:
                    sys.stderr.write(f"\n{command}: {cmd}:  No such file or directory\n")
        elif command not in list_commands:
            for path in paths:
                if os.path.isfile(f"{path}/{command}"): 
                    os.system(user_input)
                    break
            else:
                sys.stdout.write(f"{command}: not found\n")


            #sys.stdout.write(f"{command}: command not found ---\n")
    

if __name__ == "__main__":
    main()
