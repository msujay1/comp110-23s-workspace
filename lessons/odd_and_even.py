def odd_and_even(list1: list[int]) -> list[int]:
    """Function should return a list of odd and even integers"""
    i :int = 0
    list_2 : list[int] = []

    while i < len(list1):
        if list1[i] % 2 == 1 and i % 2 == 0:
            list_2.append(list1[i]) 
        else:
            i += 1
    return list_2