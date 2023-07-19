from twttr import shorten

def main():
    # Call the test functions.
    test_upper_lower()
    test_numbers()
    test_punctuation()

# Test letters uppercase & lowercase.
def test_upper_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwiTter") == "TwTtr"

# Test Numbers.
def test_numbers():
    assert shorten("tw1tt3r") == "tw1tt3r"

# Test Punctuation.
def test_punctuation():
    assert shorten("Tw.i,tter") == "Tw.,ttr"




if __name__ == "__main__":
    main()