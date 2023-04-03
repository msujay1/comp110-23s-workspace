"""Unit test for the Utils Function."""
__author__ = "730556908"

from exercises.ex05.utils import only_evens, concat, sub


def test_even_odd() -> None:
    """I am going to use a few evens and a few odds."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_evens() -> None:
    """I am going to use one even and a bunch of odds."""
    test_list: list[int] = [1, 2, 3, 5, 7, 9]
    assert only_evens(test_list) == [2]


def test_empty() -> None:
    """I am going to use am empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_same_elements_each() -> None:
    """Test concat function using the same integers in both the lists."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [1, 2, 3]
    assert concat(test_list1, test_list2) == [1, 2, 3, 1, 2, 3]


def test_differnt_elemens_each() -> None:
    """Testing the concat function suing different integers."""
    test_list1: list[int] = [1, 3, 4]
    test_list_2: list[int] = [5, 4]
    assert concat(test_list1, test_list_2) == [1, 3, 4, 5, 4]


def test_one_empty() -> None:
    """Testing concat function using one empty and one regular list."""
    test_list1: list[int] = []
    test_list2: list[int] = [1, 4, 7]
    assert concat(test_list1, test_list2) == [1, 4, 7]


def test_the_short_list() -> None:
    """Testing with minimal integers."""
    test_list: list[int] = [1, 2, 3]
    start_index: int = 1
    end_index: int = 2
    assert sub(test_list, start_index, end_index) == [2]


def test_the_long_list() -> None:
    """I will test the sub function with multiple integers."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    start_index: int = 2
    end_index: int = 5
    assert sub(test_list, start_index, end_index) ==  [3, 4, 5]


def test_empty_list() -> None:
    """Testing with no integers."""
    test_list: list[int] = []
    start_index: int = 0
    end_index: int = 4
    assert sub(test_list, start_index, end_index) == []