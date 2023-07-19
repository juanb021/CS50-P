from fuel import gauge, convert
from pytest import raises
def main():
    # Call the tests.
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    with raises(ValueError):
        convert("cat/dog")
    with raises(ZeroDivisionError):
        convert("10/0")
def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

if __name__ == "__main__":
    main()