from bank import value

def main():
    # Call test Functions.
    # Check Values.
    test_zero()
    # Check case insensitivity.
    test_twenty()
    # Check a whole phrase.
    test_hundred()

def test_zero():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLLo") == 0

def test_twenty():
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("hEy") == 20

def test_hundred():
    assert value("what's up") == 100
    assert value("WHATS'S UP") == 100
    assert value("What's UP") == 100




if __name__ == "__main__":
    main()