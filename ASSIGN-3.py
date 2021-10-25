side1 = float(input("Enter first side of triangle: "))
side2 = float(input("Enter second side of triangle: "))
side3 = float(input("Enter third side of triangle: "))

# SEMI-PERIMETER
s = (side1 + side2 + side3) / 2

# AREA OF TRIANGLE
area = round((s*(s-side1)*(s-side2)*(s-side3)) ** 0.5)
print(f"Area of triangle is {area}")
