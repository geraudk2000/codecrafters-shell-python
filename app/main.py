import sys
import os
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def relative_to_absolute(path: str) -> str:
    """
    Convert a relative path to an absolute path.
    
    Parameters:
    path (str): The relative path.
    
    Returns:
    str: The absolute path.
    """
    stack = []
    components = path.split('/')

    for component in components:
        if component in {"", "."}:
            continue
        elif component == "..":
            if stack:
                stack.pop()
        else:
            stack.append(component)
    return "/" + "/".join(stack)

def handle_echo(args: List[str]) -> None:
    """Handle the echo command."""
    sys.stdout.write(" ".join(args) + "\n")

def handle_type(args: List[str], list_commands: set, paths: List[str]) -> None:
    """Handle the type command."""
    if not args:
        sys.stdout.write("type: missing operand\n")
        return
    cmd = args[0]
    if cmd in list_commands:
        sys.stdout.write(f"{cmd} is a shell builtin\n")
    else:
        for path in paths:
            cmd_path = os.path.join(path, cmd)
            if os.path.isfile(cmd_path):
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
                return
        sys.stdout.write(f"{cmd}: not found\n")

def handle_pwd() -> None:
    """Handle the pwd command."""
    sys.stdout.write(os.getcwd() + "\n")

def handle_cd(args: List[str], home: str) -> None:
    """Handle the cd command."""
    if not args:
        target_path = home
    else:
        target_path = args[0]
        if target_path == "~":
            target_path = home
        else:
            target_path = relative_to_absolute(os.path.join(os.getcwd(), target_path))
    
    try:
        os.chdir(target_path)
    except FileNotFoundError:
        sys.stderr.write(f"cd: {args[0]}: No such file or directory\n")

def execute_external_command(command: str, paths: List[str]) -> None:
    """Attempt to execute an external command."""
    for path in paths:
        cmd_path = os.path.join(path, command)
        if os.path.isfile(cmd_path):
            os.system(command)
            return
    sys.stdout.write(f"{command}: not found\n")

def main():
    list_commands = {"echo", "type", "exit", "pwd", "cd"}
    PATH = os.environ.get('PATH', '')
    HOME = os.getenv('HOME', '/')
    paths = PATH.split(":")

    command_handlers = {
        "echo": handle_echo,
        "type": lambda args: handle_type(args, list_commands, paths),
        "pwd": handle_pwd,
        "cd": lambda args: handle_cd(args, HOME)
    }

    while True:
        try:
            sys.stdout.write("$ ")
            sys.stdout.flush()
            user_input = input().strip()
            if not user_input:
                continue
            
            command, *args = user_input.split(" ")
            if command == "exit" and args == ["0"]:
                break

            if command in command_handlers:
                command_handlers[command](args)
            else:
                execute_external_command(user_input, paths)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

