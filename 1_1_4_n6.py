
#   a114_divisible.py

# get two numbers from user

number1 = int(input("Choose a number. "))

number2 = int(input("Choose a number that is divisible by that number. "))

# loop while the numbers are not divisible (the remainder is 0)

while (number1 % number2 != 0):

  # inform user of result 
  print("L + Ratio bozo those aren't divisibile. Choose 2 more numbers.")

  # gather user input again
  
  number1 = int(input("Choose a number "))

  number2 = int(input("Choose a second number "))


# inform user of result 

print("Ur lowkey right, those numbers are divisible. ")