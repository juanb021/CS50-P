from re import search


def main():
    print(validate(input("IPv4 Address: ")))

# Expect something that looks like this "#.#.#.#"
# The numbers must be less or equal to 255 AND greater or equal than 0.
def validate(ip):
    i = 1
    if matches := search(r"^(\d\d*\d*)\.(\d\d*\d*)\.(\d\d*\d*)\.(\d\d*\d*)$", ip):
        while i <= 4:
            if 0 <= int(matches.group(i)) <= 255:
                i += 1
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()