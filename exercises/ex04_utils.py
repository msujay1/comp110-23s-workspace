"""Fun with Utils!"""
__author__ = "730556908"


def all (list: list[int], integer: int) -> bool:
    """Looking to see if the integer matches with the list"""
    if len(list) == 0:
        return False
    index: int = 0
    while index < len(list):
        if list[index] != integer:
            return False
        else:
            index += 1
    return True


def max(list:list[int]) -> int:
    """The function will return the largest integer"""
    if len(list) == 0:
        raise ValueError("max() arg is an emptly List")
    index: int = 0
    max_number: int = list[0]
    while index <= len(list) - 1:
        original_number: int = list[index]
        if (max_number < original_number):
            max_number = original_number
        index += 1
    return max_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checking to see matching integers"""
    index: int = 0
    if len(list1) != len(list2):
        return False
    while index < (len(list1 -1)) or index < (len(list2) -1 ):
        if list1[index] != list2[index]:
            return False
        else: 
            index += 1
    return True





