"""CQ04 - Dict Function Writing"""

__author__ = "730556908"

def zip(list_1: list[str], list_2:list[int]) -> dict[str,int]:
    i : int = 0
    final_list: dict[str,int] = {}
    if len(list_1) != len(list_2):
        return dict()
    if len(list_1) == 0 or len(list_2) == 0:
        return dict()
    while i < len(list_1):
        final_list[list_1[i]] = list_2[i]
        i += 1
    return final_list


    

