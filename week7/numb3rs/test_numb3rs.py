from numb3rs import validate


def main():
    test_validate()
    test_len_validate()


def test_validate():
    assert validate("121.122.123.124") == True
    assert validate("121.256.1203.124") == False
    assert validate("cat") == False

def test_len_validate():
    assert validate("121.122.123") == False
    assert validate("121.122.123.124.125") == False



if __name__ == "__main__":
    main()