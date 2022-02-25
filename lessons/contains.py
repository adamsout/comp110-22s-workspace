"""An examaple of a function that searchers through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


# Define a function named countains
# 2 paramters
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm
    # For each item in the haystack
    #   test if it is equal to the needle
    #       if so, return True
    for item in haystack:
        if item == needle:
            return True
#   After testing all the items, return False, because not found
# Returns true if the needle in haystack, false otherwise
    return False


if __name__ == "__main__":
    main()