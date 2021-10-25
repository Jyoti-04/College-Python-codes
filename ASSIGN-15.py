num = int(input("Enter a number you want to check for : "))
fact = 1
if num > 0:
    for i in range(1, num+1):
        fact = fact * i
    print(f"The factorial of given number is {fact}")
else:
    print("negative integer number can't have factorial")
