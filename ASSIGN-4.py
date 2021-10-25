import cmath

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

# DISCRIMINANT
dis = (b**2) - (4*a*c)

# WE will get two results
positive = (-b+cmath.sqrt(dis))/(2*a)
negative = (-b-cmath.sqrt(dis))/(2*a)

print(f"The Two solutions are {positive} and {negative}")
