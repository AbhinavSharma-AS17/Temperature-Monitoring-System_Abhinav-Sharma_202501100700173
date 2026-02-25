# Temperature Monitoring System


min_temp = int(input("Enter minimum temperature limit: "))
max_temp = int(input("Enter maximum temperature limit: "))

print("\nTemperature Monitoring Started")
print("Enter -1 to stop the program\n")

while True:
    temp = int(input("Enter current temperature: "))

    if temp == -1:
        print("Monitoring Stopped")
        break

   
    if temp < min_temp:
        print("Status: Temperature is BELOW minimum limit \n")

    elif temp > max_temp:
        print("Status: Temperature is ABOVE maximum limit \n")

    else:
        print("Status: Temperature is NORMAL \n")