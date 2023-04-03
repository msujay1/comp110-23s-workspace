"""Unit Test for Dictionary Functions."""
__author__ = "730556908"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_few() -> None:
    """This test will use the invert function with a few key-value pairs."""
    test_dict: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(test_dict) == {'b': 'a', 'd': 'c'}


def test_invert_more() -> None:
    """Testing function with a four value pair."""
    test_dict: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}
    assert invert(test_dict) == {'b': 'a', 'd': 'c', 'f': 'e', 'h': 'g'}


def test_blank_invert() -> None:
    """Testing the function with no key value pairs."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_short_favorite_color() -> None:
    """Testing the function with three value pairs."""
    test_dict: dict[str, str] = {'Taylor': 'green', 'Timmy': 'blue', 'Nate': 'green'}
    assert favorite_color(test_dict) == "green"


def test_long_favorite_color() -> None:
    """Testing the function with five value pairs."""
    test_dict: dict[str, str] = {'Taylor': 'green', 'Timmy': 'blue', 'Nate': 'green', 'Zyn': 'green'}
    assert favorite_color(test_dict) == "green"


def test_single_color() -> None:
    """Testing with no key pairs."""
    test_dict: dict[str, str] = {'Taylor', 'red'}
    assert favorite_color(test_dict) == 'red'


def test_short_count() -> None:
    """Testing the function with three itrems in list."""
    test_list: list[str] = ["bot", "red", "bot"]
    assert count(test_list) == {'bot': 2, 'cat': 1}

    
def test_long_count() -> None:
    """Testing the function with 5 items."""
    test_list: list[str] = ["bot", "red", "bot", "bot", "red"]
    assert count(test_list) == {'bot': 3, 'cat': 2}


def test_single_count() -> None:
    """Testing with no key pairs."""
    test_list: list[str] = {}
    assert count(test_list) == {}