def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    # Check the posible scenarios.
    check = greeting.strip().lower()
    if "hello" in check:
        ammount = 0
    elif "h" in check[0]:
        ammount = 20
    else:
        ammount = 100

    # Return the ammount.
    return ammount


if __name__ == "__main__":
    main()