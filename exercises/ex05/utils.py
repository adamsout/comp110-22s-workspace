"""EX05 - skeleton functions for function tests."""

__author__ = "730392844"


def only_evens(xs: list[int]) -> list[int]:
    """Sorts through a list of ints and returns a list of only even numbers."""
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a list beginning with index of the start value and ending with the end index value."""
    xs: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = (len(a_list) - 1)
    else: 
        end -= 1
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return xs
    i: int = start
    while i <= end:
        xs.append(a_list[i])
        i += 1
    return xs


def concat(first: list[int], last: list[int]) -> list[int]:
    """Adds two lists together in order."""
    new: list[int] = list()
    new = first + last
    return new