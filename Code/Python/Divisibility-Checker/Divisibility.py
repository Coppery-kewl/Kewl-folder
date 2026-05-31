print("Welcome to Divisibility checker by Coppery")
print()
Number = input("Number whose divisibility by another number you want to check: ")
print()
Divisibility = input("The number who you'd divide by: ")
print()
Number = float(Number)
Divisibility = float(Divisibility)
print(f"""Is...

    {Number} divisible by {Divisibility}?

    Answer:""")
print()
if Number % Divisibility == 0 : print(f"Yes, {Number} is divisible by {Divisibility}.")
else : print(f"No, {Number} is not divisible by {Divisibility}.")
print()
print("Thanks for using this :]")
