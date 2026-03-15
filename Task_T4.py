'''TaskPY200_T4: Write program to check password strength rules
Input a string s (assume lowercase/uppercase/digits may appear)
Now check: if the string contains full fills and print final output: valid (STRONG) or Invalid
password (WEAK)
1. length >= 8
2. has at least 1 digit
3. has at least 1 uppercase
4. has at least 1 lowercase
Print “STRONG” else “WEAK”'''

Pswd = input('Enter Your Password: ')

has_digit = False
has_upper = False
has_lower = False 

for Char in Pswd:
    if Char.isdigit():
        has_digit=True
    elif Char.isupper():
        has_upper=True
    elif Char.islower():
        has_lower = True
        
if len(Pswd)>= 8 and has_digit and has_upper and has_lower:
    print("Valid Password STRONG")

else:
    print("Invalid Password Weak")
        