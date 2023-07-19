from lines import check_line, get_lines

def main():
    test_check_line()
    test_get_lines()

def test_check_line():
    assert check_line("def main():") == True
    assert check_line("#") == False
    assert check_line("") == False

def test_get_lines():
    assert get_lines("hello.py") == 5
    assert get_lines("meal.py") == 23
