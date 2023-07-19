def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters.
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # The first number used cannot be a ‘0’.
    i = 2
    while i < len(s):
        if s[i].isdigit():
            if int(s[i]) == 0:
                return False
            else:
                i += 1
                break
        i += 1

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    while i < len(s):
        if s[i].isalpha():
            return False
        i += 1

    # No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False

    # If all test are ok, the plate is valid.
    return  True


if __name__ == "__main__":
    main()