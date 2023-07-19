from um import count


def main():
    test()


def test():
    assert count("Yummy") == 0
    assert count("thanks for um the meal") == 1
    assert count("my name is UM Juan") == 1
    assert count("um, um. yummy") == 2


if __name__ == "__main__":
    main()