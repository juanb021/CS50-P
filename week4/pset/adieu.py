# Import the libraries.
import inflect

p = inflect.engine()

def main():
    # Create a list to store all of the names.
    list_of_names = []
    # Loop Forever.
    while True:
        # Get the user input.
        try:
            name = input("Name: ")
            list_of_names.append(name)
        except EOFError:
            # Create a new line and stop the loop.
            print()
            break
    # Use the p.join method to print.
    output = p.join(list_of_names)
    print("Adieu, adieu, to " + output)

if __name__ == "__main__":
    main()