import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()
    list_commands = set()
    # Wait for user input
    command = input()
    if command not in list_commands:
        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
