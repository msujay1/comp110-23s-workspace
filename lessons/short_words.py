def short_words(list1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list = []
    for value in list1:
        if len(value) < 5:
            new_list.append(value)
        if len(value) >= 5:
            print(f'{value} is too long!')
    return new_list