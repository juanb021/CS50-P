import re
import sys


def main():
    # Test should be Yummy um um, um. um?
    print(count(input("Text: ")))

# Must count um um, um.
# Ignore Yummy.
def count(s):
    counter = re.findall(r"\b(um)\b[\.\?,]?", s, re.IGNORECASE)
    return len(counter)

if __name__ == "__main__":
    main()