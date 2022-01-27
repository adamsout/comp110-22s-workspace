"""EX02 - One Shot Wordle."""

__author__ = "730392844"

secret: str = "python"  # secret word
l_secret: str = str(len(secret))  # length of secret word
i_secret: int = 0  # index of secret word

guess: str = input(f"What is your {l_secret}-letter guess? ")  # user guess
i_guess: int = 0  # index of user guess

WHITE_BOX: str = "\U00002B1C"  # white emoji
GREEN_BOX: str = "\U0001F7E9"  # green emoji
YELLOW_BOX: str = "\U0001F7E8"  # yellow emoji
guess_emoji: str = ""  # emoji string of user guess

alt_character: bool = False  # for counting for yellow box
i_alt: int = 0  # if character is in word but not correct index, this will keep track of the index when counting for yellow box

# if the word guessed by the user is not the length of the secret word, it tells the user to input a new word
while len(guess) != len(secret):
    guess = str(input(f"That was not {l_secret} letters! Try again: "))

if len(guess) == len(secret):  # if the length of user guess is equal to the lenght of the secret word, it checks each index to see if there is a matching letter and adds a green box to the emoji string
    while i_guess < int(l_secret):
        if guess[i_guess] == secret[i_secret]:
            guess_emoji = guess_emoji + GREEN_BOX
        else:  # after checking for a matching letter in a mathcing index, it will check for matching letters in the word and add a yellow box to the emoji string
            i_alt = 0
            while alt_character is not True and i_alt < len(secret):
                if guess[i_guess] == secret[i_alt]: 
                    alt_character = True
                else:  # if there is no matching letter, it will add a white box to the emoji string
                    i_alt += 1
            if alt_character is True:
                guess_emoji += YELLOW_BOX
                alt_character = False
            else:
                guess_emoji += WHITE_BOX
        i_guess += 1
        i_secret += 1
            
    if guess != secret:  # if the user guess matches the length of the secret word but is not the word
        print(guess_emoji)
        print("Not quite. Play again soon!")
    else:  # if the user guess matches the secret word
        print(guess_emoji)
        print("Woo! You got it!")
