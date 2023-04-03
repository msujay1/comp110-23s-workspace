"""EX07 Dictionary."""
__author__ = "730556908"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """This function inverts the values in the dictionary."""
    dict2: dict[str, str] = {}
    for elem in dict1:
        if dict1[elem] in dict2:
            raise KeyError("You cannot have duplicate keys!")
        dict2[dict1[elem]] = elem
    return dict2


def favorite_color(my_dict: dict[str, str]) -> str:
    """Returns color that appears the most."""
    color_count: dict[str, int] = {}
    for elem in my_dict:
        color = my_dict[elem]
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1
    max_count: int = 0
    popular_color: str = ""
    for color in color_count:
        count = color_count[color]
        if count > max_count:
            max_count = count
            popular_color = color
    return popular_color


def count(list1: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1