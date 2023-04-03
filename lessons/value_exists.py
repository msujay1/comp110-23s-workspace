def value_exists(dictionary: dict[str,int], value: int) -> bool:
    """The Function should return True if the int exists as a value in the dictionary and False otherwise."""
    exists: bool = False
    for elem in dictionary:
        if dictionary[elem] == value:
            exists = True
    return exists


    