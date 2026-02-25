# Temperature Monitoring System

# Input minimum and maximum temperature limits
min_temp = int(input("Enter minimum temperature limit: "))
max_temp = int(input("Enter maximum temperature limit: "))

print("\nTemperature Monitoring Started")
print("Enter -1 to stop the program\n")

# Loop to keep checking temperature
while True:
    
    # Input current temperature
    temp = int(input("Enter current temperature: "))

    # Stop condition
    if temp == -1:
        print("Monitoring Stopped")
        break

    # Compare temperature with limits
    if temp < min_temp:
        print("Status: Temperature is BELOW minimum limit \n")

    elif temp > max_temp:
        print("Status: Temperature is ABOVE maximum limit \n")

    else:
        print("Status: Temperature is NORMAL \n")
