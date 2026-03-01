#In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it like so:
#Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

#x = (-b ± sqrt(b²-4ac))/(2a).
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

root1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
root2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print("")
print(f"The roots are {root1} and {root2}")

