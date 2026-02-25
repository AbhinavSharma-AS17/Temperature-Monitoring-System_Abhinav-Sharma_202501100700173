import random
import time

# Take maximum temperature limit
max = int(input("Enter maximum temperature in Celsius: "))

# Take minimum temperature limit
min = int(input("Enter minimum temperature in Celsius: "))

# Number of temperature readings to take
r = int(input("Enter number of readings to take: "))

mean = 0  # To store sum of temperatures

# Generate temperature readings
for i in range(1, r + 1):
    a = random.randint(min, max)  # Generate random temperature
    print("READING", i, ": The temperature is:", float(a), "C")
    mean = mean + a               # Add temperature to sum
    time.sleep(2)                 # Wait for 2 seconds

# Display average temperature
print("Experimental value obtained:", mean / r, "C")
