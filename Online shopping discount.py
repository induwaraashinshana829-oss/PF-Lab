

pre_member = int(input("Press 1 toyr premium/Press 0 otherwisw :"))

if pre_member == 1 :
    tot = float(input("Enter purchase ammount?"))

    if tot >= 10000 :
        dis = tot * 20/100
    print("Discount is 20% = ",dis)
    
    else : 
        dis = tot * 10/100
        print("Discount of 10% = "dis)

else :
    print("No Discount")
        
