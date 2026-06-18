

count - 1
safe_count = 0
faild_count = 0

while count <= 4 :
    temp = float(input("Enter Engine Temperature :"))
    if 200 < temp and temp < 850 :
        print("Engine ",count," is Safe ! ")
        safe_count = safe_count + 1
    else :
        print("Engine ",count," is required maintance ! ")
        failed_count = faild_count + 1

   count = count + 1 

print("Number of safe Engines : ",safe_count)
print("Number of fault Engines :",failed_count)


