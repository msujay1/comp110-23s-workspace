"""EX08."""
__author__ = "730556908"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts and header keys."""
    result: list[dict[str, str]] = []
    file_handle= open(filename, "r", encoding= "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result
    

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    result: list[str] = []
    # step through table
    for row in table:
        #save every value under the key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats our data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result
    

def head(dict1: dict[str, list[str]], numb: int) -> dict[str, list[str]]:
    """Produces a new column wurh only a specific subset of the original columns."""
    dict2: dict[str, list[str]] = {}
    for elem in dict1:
        list1: list[str] = []
        if numb > len(dict1[elem]):
            numb = len(dict1[elem])
        for el in range(numb):
            list1.append(dict1[elem][el])
        dict2[elem] = list1
    return dict2


def select(dict1: dict[str, list[str]], list1: list[str]) -> dict[str, list[str]]:
    """Produces a new column based on a table with only a specific subset of the original columns."""
    dict2: dict[str, list[str]] = {}
    for elem in list1:
        dict2[elem] = dict1[elem]
    return dict2


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column with two column- based tables combined."""
    dict3: dict[str, list[str]] = {}
    for elem in dict1:
            dict3[elem] = dict1[elem]
    for elem in dict2:
        if elem in dict3:
            dict3[elem] += dict2[elem]
        else:
            dict3[elem] = dict2[elem]
    return dict3


