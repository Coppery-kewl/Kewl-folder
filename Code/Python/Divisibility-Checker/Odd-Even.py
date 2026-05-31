print("Welcome to Odd/Even, Number has to be number only, no letter or symbols")
user_number=input("Number: ")
user_number=int(user_number)
odd_or_even_answer=user_number%2
if odd_or_even_answer==0:print("Even!")
else:print("Odd!")
