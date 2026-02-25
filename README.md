# Temperature Monitoring System

## Problem Statement
A temperature monitoring system is required to check whether the current
temperature is within the acceptable range.

The system should:
- Accept minimum and maximum temperature limits
- Accept current temperature values from the user
- Compare the temperature with the limits
- Display appropriate status messages
- Stop monitoring when `-1` is entered

---

## Approach
1. Take minimum and maximum temperature limits from the user.
2. Start the monitoring process using a loop.
3. Accept the current temperature from the user.
4. Compare the entered temperature with the given limits.
5. Display whether the temperature is normal, below, or above the limit.
6. Stop the program when the user enters `-1`.

---

## Sample Output

Enter minimum temperature limit: 20  
Enter maximum temperature limit: 30  

Temperature Monitoring Started  
Enter -1 to stop the program  

Enter current temperature: 18  
Status: Temperature is BELOW minimum limit  

Enter current temperature: 25  
Status: Temperature is NORMAL  

Enter current temperature: 35  
Status: Temperature is ABOVE maximum limit  

Enter current temperature: -1  
Monitoring Stopped  

---

## Author
Name: Abhinav Sharma