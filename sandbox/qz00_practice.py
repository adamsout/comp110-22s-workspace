a: str = "qwerty"
b: str = "3.14"
c: str = a[0] + a[len(b)]
print(c)

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
if choice >= 50:
    if choice > 75:
        print("C")
    if choice <= 75:
        print("D")