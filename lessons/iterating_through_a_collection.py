"""Example of looping through all characters of a string."""

user_string: str = input("Give me a string! ")

# varaible i is a commmon counter variable name. i = iteration
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")

print(not True and not True)