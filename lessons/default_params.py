"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Example of a defeault parameter where y and z are 0 by default."""
    """Every parameter after the first default parameter must be a default parameter."""
    return x + y + z


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))