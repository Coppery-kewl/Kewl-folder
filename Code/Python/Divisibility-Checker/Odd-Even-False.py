print ("Welcome to Odd/Even but EVILLLLLL (means it is liar), Number has to be number only, no letter or symbols")
user_number = int(input ("Number: "))
user_number -= 1
odd_or_even_answer = int (user_number) % 2
if odd_or_even_answer == 0 : print ("Even!")
else : print ("Odd!")
