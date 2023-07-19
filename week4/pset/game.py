# Import the necesary libraries.
import random

def main():
    # Loop Forever.
    while True:
        try:
            # Ask the user the dificulty of the game.
            n = int(input("Level: "))

            if n < 1:
                print("Difficulty level must be 1 or more.")
            else:
                break

        except ValueError:
            print("Must enter a integer.")

    # Generate a random number for the user to guess.
    number = random.randint(1, n)

    # Loop Forever.
    while True:
        try:
            guess = int(input("Guess: "))

            if guess == number:
                print("Just right!")
                break
            elif guess < number:
                print("Too small!")
            else:
                print("Too large!")


        except ValueError:
            print("Must enter a integer.")

if __name__ == "__main__":
    main()