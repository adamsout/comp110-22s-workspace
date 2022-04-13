"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730392844"


class Simpy:
    """Defines a class called Simpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute."""
        self.values = values
 
    def __str__(self) -> str:
        """Returns strings."""
        return f"Simpy({self.values})"

    def fill(self, value: float, amt: int) -> None:
        """Fills Simpy's values with a specific number of repeating values."""
        i: int = 0
        self.values = []
        while i < amt:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a list of values that increment with the given amount."""
        assert step != 0.0
        self.values = []
        while start < stop or stop < start:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Compute and return the sum in the values attribute."""
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Produces a list that adds every value in the in the first list to the value of the second list or float."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs)
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Produces a list that takes the power to every value in the in the first list to the value of the second list or float."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs)
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask that tests each value for whether or not it is equal to the input."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask that tests each value for whether or not it is greater than the input."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return the value associated with the inputed index."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result = Simpy([])
            assert len(self.values) == len(rhs)
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result