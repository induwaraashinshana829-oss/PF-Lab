

weight = float(input("Enter the Weight(kg): "))

if weight <= 20 :
    print("No Extra Charges")
             
elif weight <= 30 :
    extra_charge = (weight-20) * 200
    print("Extra Charge is:Rs. ",extra_charge)

else :
    print("Laggage is Not Allowed")
     
   
