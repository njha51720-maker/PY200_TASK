'''TaskPY200_T2: Write python program to check if number is positive, negative, or zero.
Using formatted string printing show message like : “Your entered number {} was negative ,
how ever positive value of your number is {}
'''


n=int(input("Enter Your Number: "))
if n>0:
    print(f"Your Entered Number {n} was Positive, However positive value of your number is {n}")

elif n<0:
    print(f"Your Entered Number {n} was negative, However positive value of your number is {-n}")

else:
    print("Your Entered Number was {0} However positive value is 0 ")    