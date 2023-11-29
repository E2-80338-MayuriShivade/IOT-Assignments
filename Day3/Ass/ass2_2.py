#A = float(input("Enter Amount = ")) 
P = float(input("Enter Principal = "))
R = float(input("Enter Rate = "))
T = float(input("Enter Time = "))
 
Amount=P*(1+(R/100))**T
CI=Amount-P
print(f"CI is",CI)

Amount1=P*(pow((1+R/100),T))
CI1=Amount1-P
print(f"CI is",CI1)
