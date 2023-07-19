from datetime import date
import inflect
import sys


def main():
    print(minutes_passed(input("Birth day: ").split("-")))


def minutes_passed(s):

    # Create the inflect engine.
    p = inflect.engine()

    # Convert the input into a integer.
    try:
        year, month, day = int(s[0]), int(s[1]), int(s[2])
    except ValueError:
        sys.exit("Invalid Date")

    # Create a object of the class "Date".
    bd = date(year, month, day)
    tday = date.today()
    diff = int((tday - bd).total_seconds()/60)

    # Convert the info into a string, return the message without the "and"
    msg = p.number_to_words(diff, andword="") + " minutes"
    return msg.capitalize()

if __name__ == "__main__":
    main()