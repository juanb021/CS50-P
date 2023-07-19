from working import convert
from pytest import raises


def main():
    test1()
    test2()


def test1():
    assert convert("5 AM to 5 PM") == "05:00 to 17:00"
    assert convert("5:30 AM to 5:30 PM") == "05:30 to 17:30"

def test2():
    with raises(ValueError):
        convert("5 AM - 5 PM")
    with raises(ValueError):
        convert("5:70 AM to 5:70 PM")


if __name__ == "__main__":
    main()