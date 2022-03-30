"""Dictionary related utility functions."""

__author__ = "730392844"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """A function that produces a list of strings from a given column from a table."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """A function that when given a column-based table, it returns only a specific number of rows 'n' for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        new: list[str] = []
        i: int = 0
        if n >= len(table):
            return table
        while i < n:
            new.append(table[column][i])
            i += 1
        result[column] = new
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        column_value: list[str] = table[column]
        result[column] = column_value
    return result


def concat(first: dict[str, list[str]], last: dict[str, list[str]]) -> dict[str, list[str]]:
    """Adds two two column-based tables together."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]   
    for column in last:
        if column in result and first[column] != last[column]:
            result[column] += last[column]
        else:
            result[column] = last[column]
    return result
        

def count(values: list[str]) -> dict[str, int]:
    """Counts the amount of times each str in values appears."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in result:
            result[values[i]] += 1
        else:
            result[values[i]] = 1
        i += 1
    return result


def sorts(values: dict[str, int]) -> dict[str, int]:
    """Sorts through values and puts the keys in order."""
    result: dict[str, int] = {}
    if "" in values:
        result[""] = values[""]
    i: int = 1
    while i <= 7:
        result[str(i)] = values[str(i)]
        i += 1
    return result
