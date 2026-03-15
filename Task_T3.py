'''TaskPY200_T3: Write program to calcite Electricity Bill Slabs. User enters a bill unit and
gets the total bill according to following logic.
Input: units
Rates:
• First 100 @ 2/unit
• Next 100 (101–200) @ 3/unit
• Next 300 (201–500) @ 5/unit
• Above 500 @ 8/unit
Add fixed charge 50 if units > 0
Print total bill
'''

units=int(input("Enter The Units: "))

bill=0

if units <=100:
    bill= units*2

elif units <=200:
    bill = (100*2) + ((units-100)*3)
    
elif units <=500:
    bill = (100*2) + (100*3) + ((units-200)*5)
    
else:
    bill=(100*2) + (100*3) + (300*5) + ((units-500)*8)
    
if units >0:
    Total_bill= bill + 50
    
print(f"Total bill is {Total_bill}")