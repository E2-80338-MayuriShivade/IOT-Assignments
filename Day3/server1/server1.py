import temperature.create
import temperature.read

temp= float(input("Enter temperature : "))
loc = input("Enter location : ")
temperature.create.insert_temperature(temp,loc)

temps = temperature.read.get_temperature()
for temp in temps:
    print(temp)
