print("Welcome to Divisibility numm ber! It tells you the divisibility of a number from 2 to 10! Number must ONLY be a number!")
user_number = input("Number: ")
user_number = int(user_number)
by2 = user_number % 2
by3 = user_number % 3
by4 = user_number % 4
by5 = user_number % 5
by6 = user_number % 6
by7 = user_number % 7
by8 = user_number % 8
by9 = user_number % 9
by10 = user_number % 10
print(f"{str(user_number)} is divisible by...")
if by2 == 0 : print("2: Yes")
else : print("2: No")
if by3 == 0 : print("3: Yes")
else : print("3: No")
if by4 == 0 : print("4: Yes")
else : print("4: No")
if by5 == 0 : print("5: Yes")
else : print("5: No")
if by6 == 0 : print("6: Yes")
else : print("6: No")
if by7 == 0 : print("7: Yes")
else : print("7: No")
if by8 == 0 : print("8: Yes")
else : print("8: No")
if by9 == 0 : print("9: Yes")
else : print("9: No")
if by10 == 0 : print("10: Yes")
else : print("10: No")
print("Thank You for using this :) - Coppery")
