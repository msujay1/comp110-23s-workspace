"""EX05 - Utils."""

__author__ = "730556908"


def only_evens(input: list[int]) -> list[int]:
    """Returns input's even numbers."""
    list_evens: list[int] = list()
    for idx in range( 0, len(input)):
        if input[idx] % 2 == 0:
            list_evens.append(input[idx])
    return list_evens


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists of integers , concat combines them into one list."""
    new_list: list[int] = list()
    new_list += list1
    new_list += list2
    return new_list


def sub(list1: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    list2: list[int] = list()
    if len(list1) == 0 or start_index >= len(list1) or end_index <= 0:
        return list2
    if start_index < 0:
         start_index = 0
    if end_index > len(list1):
        end_index = len(list1)
    for idx in range(start_index, end_index):
        list2.append(list1[idx])
    return list2