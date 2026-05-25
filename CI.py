p = float(input("Enter Amount ?"))
r = float(input("Enter Annual Interest Rate ?"))
n = float(input("Enter Years ?"))

CI = p * ((100+r)/100)**n


print ("Compound Interest is", CI)
