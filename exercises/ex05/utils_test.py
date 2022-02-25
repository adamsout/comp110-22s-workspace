"""EX05 - Function tests for utils."""

__author__ = "730392844"

from utils import only_evens, sub, concat


# tests for only_evens
def test_only_evens_empty() -> None:
    """Tests only_evens for being an empty list."""
    xs: list[int] = list()
    assert only_evens(xs) == list()


def test_only_evens_all_evens() -> None:
    """If only_evens was given a list of all evens, would it return all of them."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_many_items() -> None:
    """Tests if only_evens with many items to see if it work with many items."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


# tests for sub
def test_sub_one_item() -> None:
    """Tests sub to see if it will return an empty list when necessary."""
    a_list: list[int] = [10]
    assert sub(a_list, 1, 3) == []


def test_sub_bad_indicies() -> None:
    """Tests sub to see if it will return the correct list even when indicies are out of range."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -1, 7) == [10, 20, 30, 40]


def test_sub_big_list() -> None:
    """Tests if sub will return correct list when given a big list with a wide range of indicies."""
    a_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(a_list, 2, 9) == [2, 3, 4, 5, 6, 7, 8]


# tests for concat
def test_concat_empty() -> None:
    """Tests concat to see if it will return empty list when adding empty lists."""
    first: list[int] = list()
    last: list[int] = list()
    assert concat(first, last) == list()


def test_concat_long_list() -> None:
    """Tests concat to see if it will add big lists corectly."""
    first: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    last: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert concat(first, last) == [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_one_empty() -> None:
    """Tests to see if concat can add an empty list to a full list."""
    first: list[int] = list()
    last: list[int] = [1, 2, 3, 4]
    assert concat(first, last) == [1, 2, 3, 4]