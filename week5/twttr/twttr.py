def main():
    username = input("Input: ")
    print(f"Output: " + shorten(username))


def shorten(text):
    no_vowels = ""
    # Loop trough the word
    for letter in text:
        # Check if is not a vowel
        if not letter.lower() in ['a', 'e' , 'i', 'o', 'u']:
            # Add the letter to the word with no vowels
            no_vowels += letter
    # Return the word with no vowels
    return no_vowels




if __name__ == "__main__":
    main()