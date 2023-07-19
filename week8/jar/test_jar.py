from jar import Jar
from pytest import raises

def test_init():
    jar = Jar(6)
    assert jar.capacity == 6
    assert jar.size == 0

    jar = Jar(6,3)
    assert jar.capacity == 6
    assert jar.size == 3

    with raises(ValueError):
        assert Jar(-2)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == '🍪'

def test_deposit():
    jar = Jar(12, 5)
    jar.deposit(3)
    assert jar.size == 8

    jar = Jar()
    with raises(ValueError):
        jar.deposit(15)

def test_withdraw():
    jar = Jar(12, 5)
    jar.withdraw(3)
    assert jar.size == 2

    with raises(ValueError):
        jar.withdraw(15)
