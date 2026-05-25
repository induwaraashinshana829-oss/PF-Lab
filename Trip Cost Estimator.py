
distance_traveled=float(input("Enter the Travell Distance ? "))
fuel_efficiency=int(input("Enter the Fuel Efficiency ? "))
fuel_price_pre_liter=int(input("Enter the Pre Liter Price ? "))
highway_charge=float(input("Enter the Highway Charge ? "))

fuel_used=distance_traveled/fuel_efficiency
fuel_cost=fuel_used*fuel_price_pre_liter
final_trip_cost=fuel_cost+highway_charge

print("Fuel Used is " ,fuel_used)
print("Fuel Cost is " ,fuel_cost)
print("Final Trip Cost is " ,final_trip_cost)
