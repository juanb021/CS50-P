from plates import is_valid


def main():
    # Call test.

    test_alpha()
    test_len()
    test_placement()
    test_numalpha()

def test_alpha():
    assert is_valid("12lpa") == False


def test_len():
    assert is_valid("a") == False
    assert is_valid("aeioulq") == False

def test_placement():
    assert is_valid("ae12aw") == False
    assert is_valid("aeqd0") == False


def test_numalpha():
    assert is_valid("A5") == False
    assert is_valid('ABC.12') == False



if __name__ == "__main__":
    main()