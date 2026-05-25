
room_charge=int(input("Enter the Room Charge Per Day"))
number_of_days=int(input("Enter the Number Of Days"))
food_charge=int(input("Enter the Food Charge"))

sub_total=(room_charge*number_of_days)+food_charge
service_charge=sub_total*0.1
final_bill=sub_total+service_charge

print("Sub Total is" , sub_total )
print("Servise Charge is" , service_charge)
print("Final Bill is" , final_bill)

