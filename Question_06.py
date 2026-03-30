'''TaskPY200_T6: Find the Smallest Number With “Digit Constraints”
Input: N
Find smallest number x in 1..N such that:
• sum of digits of x is divisible by 7
• x contains exactly two 3s
• x does not contain digit 0
If none, print -1. 
'''

N=int(input("Enter the number: "))

smallest=-1                                        #Initalalize smallest to -1

for x in range(1,N+1):
    if('0' not in str(x)):                           # converted x to string and represents the digit '0' is not present in str(x)
        if(str(x).count('3')==2):                    #represents the count of '3' is equal to 2 in str(x)
            if((sum(int(digit) for digit in str(x)))%7==0):      #str(x) converted to individual string digit and then converted to integer and then sum is calculated 
                smallest=x                               #if conditions satisfied then smallest updated to x
                break                                    #break the loop once the smallest number is found

print("The smallest number is: ", smallest)              
               
                
                
    
                
    