from project import U_data, generate, get_data
from pytest import raises

def main():
    test_generate_default()
    test_generate_less()
    test_generate_more()
    test_str()
    test_u_data()


def test_generate_default():
    password = generate(12)
    assert len(password) == 12

def test_generate_less():
    password = generate(8)
    assert len(password) == 8

def test_generate_more():
    password = generate(16)
    assert len(password) == 16

if __name__ == '__main__':
    main()