import sys

def main():
    # Check the argv.
    check_argv()
    # Get the prompt from the user's input & Count the number of lines.
    lines = get_lines(sys.argv[1])
    print(lines)

def check_argv():
    # Check the ammount of elements in the argv.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if its a python file.
    if not ".py" in sys.argv[1]:
        sys.exit("Not a Python file")

def get_lines(a):
    # Open the Python file & and check that it exists.
    try:
        with open(a, "r") as file:
            counter = 0
            list_lines = []

            # Put the file in a variable
            lines = file.readlines()

            # Load the lines on a list.
            for line in lines:
                list_lines.append(line.lstrip().rstrip())

            # Check the list.
            for item in list_lines:
                if check_line(item):
                    counter += 1
            return counter

    # If the file doesnt Open, it doesnt exists.
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_line(a):
    if a.startswith("#") or a == "":
        return False
    else:
        return True


if __name__ == "__main__":
    main()