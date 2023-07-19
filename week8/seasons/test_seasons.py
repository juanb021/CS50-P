from seasons import minutes_passed
from pytest import raises

def main():
    test_minutes()

def test_minutes():
    assert minutes_passed([2023, 3, 13]) == "One thousand, four hundred forty minutes"
    with raises(ValueError):
        minutes_passed([10000, 2, 18])

if __name__ == "__main__":
    main()