"""EX06 - Dictionary functions."""

__author__ = "730392844"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """When given a dictionary, it inverts the keys and values."""
    inv_dict: dict[str, str] = {}
    for key in dictionary:
        value: str = dictionary[key]
        if value in inv_dict:
            raise KeyError
        else:
            inv_dict[value] = key
    return inv_dict


def favorite_color(colors: dict[str, str]) -> str:
    """When given a dictionary of people and their fav color, it returns the most popular color."""
    i: int = 0
    col: dict[str, int] = {}
    fav_col: str = ""
    for key in colors:
        if colors[key] in col:
            col[colors[key]] += 1
        else:
            col[colors[key]] = 1
    for key in col:
        if col[key] > i:
            i = col[key]
            fav_col = key
    return fav_col


def count(values: list[str]) -> dict[str, int]:
    """When given a list of strs, it will rerturn a dictionary with the keys being the strs from the list and the value being how many times each value appears in the list."""
    i: int = 0
    counter: dict[str, int] = {}
    while i < len(values):
        if values[i] in counter:
            counter[values[i]] += 1
        else:
            counter[values[i]] = 1
        i += 1
    return counter