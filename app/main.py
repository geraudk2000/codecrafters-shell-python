import sys
import os

def relative_to_absolute(path):
    stack = []

    path = path.split('/')

    for file in path:
        if file == "." or file == "":
            continue
        elif file == "..":
            if stack:
                stack.pop()
        else: 
            stack.append(file)
    return "/" + "/".join(stack)



def main():
    # Uncomment this block to pass the first stage
    
    list_commands = set(["echo", "type", "exit", "pwd", "cd"])
    PATH = os.environ.get('PATH')
    HOME = os.getenv('HOME')
    # Wait for user input
    print(HOME)
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
                if cmd == "~": 
                    os.chdir(HOME)
                    continue

                actual_path = os.getcwd()
                new_path = os.path.join(actual_path, cmd) 
                path_absolute = relative_to_absolute(new_path)
                try:
                    os.chdir(path_absolute)
                    continue
                except Exception as e:
                    sys.stderr.write(f"{command}: {cmd}: No such file or directory\n")
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
