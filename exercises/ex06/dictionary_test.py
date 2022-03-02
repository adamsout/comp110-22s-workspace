"""EX06 - Test functions for dictionary."""

__author__ = "730392844"

from dictionary import invert, favorite_color, count 


# tests for invert
def test_invert_empty() -> None:
    """Tests invert for empty dictionar."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_invert_small() -> None:
    """Tests invert with dict with multiple values to raise key error."""
    small_list: dict[str, str] = {"Kris": "Jordan", "Adam": "Souter"}
    assert invert(small_list) == {"Jordan": "Kris", "Souter": "Adam"}


def test_invert_long() -> None:
    """Tests invert with a long dict."""
    long: dict[str, str] = {"a": "z", "b": "y", "c": "x", "e": "w"}
    assert invert(long) == {"z": "a", "y": "b", "x": "c", "w": "e"}


# Tests for favorite_color
def test_favorite_color_empty() -> None:
    """Tests favorite_color for empty dict."""
    empty: dict[str, str] = {}
    assert favorite_color(empty) == ""


def test_favorite_color_multiple_colors() -> None:
    """Tests favorite_color for small dict."""
    small: dict[str, str] = {"adam": "blue", "jackson": "blue", "will": "green", "ben": "green"}
    assert favorite_color(small) == "blue"


def test_favorite_single_values() -> None:
    """Tests favorite_color for keys with no same values."""
    xs: dict[str, str] = {"adam": "blue", "jackson": "green", "will": "black", "ben": "red"}
    assert favorite_color(xs) == "blue"


# Tests for count.
def test_count_empty() -> None:
    """Tests count when given empty list."""
    empty: list[str] = []
    assert count(empty) == {}


def test_count_no_matching() -> None:
    """Tests count when given a list with no matching strs."""
    none: list[str] = ["a", "b", "c", "d"]
    assert count(none) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_all_matching() -> None:
    """Tests count when given one str multiple times."""
    all: list[str] = ["a", "a", "a", "a"]
    assert count(all) == {"a": 4}