# This Age calculator is aimed
# at calculating the real time age of our users
from datetime import date
# Get the current year
Current_Year = date.today().year
 # Ask the user for their birth year
Birth_Year = int(input("Enter your birth year: "))
 # Calculate age 
age = Current_Year - Birth_Year
 # Show Result
print(f"you are {age} Year old ")