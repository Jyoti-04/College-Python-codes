def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation you want to perform")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    ch=input("enter your choice (1/2/3/4): ")
    if ch in ('1','2','3','4'):
        num1 = float(input("enter first number :"))
        num2 = float(input("enter first number :"))

    if ch == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif ch == '2':
        print(num1, "-", num2, "=", substract(num1, num2))

    elif ch == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif ch == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    next_calculation = input("Do you want to do more calculations?(yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("enter input")
