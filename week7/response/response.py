from validator_collection import validators, checkers

def main():
    print(valid((input("What's your email adress? "))))


def valid(s):
    try:
        response = validators.email(s)
        return "Valid"
    except:
        return "Invalid"

# Optional solution.
def optional(s):
    response = checkers.is_email(s)
    if response:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()