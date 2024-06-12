# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input('Enter a year: '))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"'{year}' is not a leap year")
else:
    print(f"'{year}' is not a leap year")

year1 = int(input('Enter a year: '))
if year1 % 4 == 0 and year1 % 100 == 0:
    if year1 % 400 == 0:
        print(f"{year1} is a leap year")
else:
    print(f"{year1} is not a leap year")