


units = int(input("Enter Units: "))

if units <= 30 :
        total_bill = units * 20
else :
    if units <= 60 :
        total_bill = 30 * 20 + (units - 30) * 40
    else:
        total_bill = 30 * 20 + 30 * 40 + (units - 60) * 60
        
print("Total Bill: Rs. ",total_bill)
