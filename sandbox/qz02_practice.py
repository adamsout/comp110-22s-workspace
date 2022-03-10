"""qz02 practice."""


# 24
def vowels_and_threes(word: str) -> str:
    """blah."""
    i: int = 0
    is_vowel: bool = False
    new: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    j: int = 0
    while i < len(word):
        j = 0
        is_vowel = False
        while j < len(vowels):
            if word[i] == vowels[i]:
                is_vowel = True
            j += 1
        if i % 3 == 0 and is_vowel:
            # Do nothing
            new += ""
        elif i % 3 == 0:
            new += word[i]
        elif is_vowel:
            new += word[i]
        i += 1
    return new


def main() -> None:
    """blah."""
    list1: str = "comp110"
    print(vowels_and_threes(list1))


if __name__ == "__main__":
    main()