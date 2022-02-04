"""EX03 - Wordle."""

__author__ = "730392844"


def contains_char(user_guess: str, char_in_guess: str) -> bool:
    """Checking user_guess for char_in_guess."""
    assert len(char_in_guess) == 1
    i_guess: int = 0
    while i_guess < len(user_guess):
        if char_in_guess != user_guess[i_guess]:
            i_guess += 1
        else:
            return True
    return False


def emojified(user_guess: str, secret: str) -> str:
    """Returns an emoji string that corresponds with the secret and guess."""
    assert len(user_guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"  # white emoji
    GREEN_BOX: str = "\U0001F7E9"  # green emoji
    YELLOW_BOX: str = "\U0001F7E8"  # yellow emoji
    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if user_guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, user_guess[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(len_guess: int) -> str:
    """User enters a guess and it checks and requires the correct amount of characters."""
    user_guess: str = input(f"Enter a {len_guess} character word: ")
    while len(user_guess) != len_guess:
        user_guess = input(f"That wasn't {len_guess} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret: str = "codes"
    n: int = 0  # number of the guess player is on
    won: bool = False
    while n < 6 and won is False: 
        n += 1
        print(f"=== Turn {n}/6 ===")
        user_guess: str = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print(f"You won in {n}/6 turns!")
            won = True
    if won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()