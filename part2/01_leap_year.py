#Please write a program which asks the user for a year, and prints out the next leap year.
year = int(input("Year:"))
yearf = year

while True:
    year += 1

    if year%400==0:
        break

    elif year%100!=0 and year%4==0:
        break

print(f"The next leap year after {yearf} is {year}")