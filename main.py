running = True

print("\nWelcome to the Pythagorean Triples Checker!\n")

while running:
    print("Please enter the lengths of each side of a triangle.\n")

    side1 = int(input("First side:"))
    side2 = int(input("Second side:"))
    side3 = int(input("Last side:"))

    sides = [side1, side2, side3]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("\nThat's a pythagorean triple!")
    else:
        print("\nThat isn't a pythagorean triple.")

    print("\nWould you like to check another set of numbers? Y/N\n")
    ans = input()
    if ans.lower() == "y":
        continue
    else:
        break

