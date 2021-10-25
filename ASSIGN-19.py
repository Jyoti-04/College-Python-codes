lower_range = int(input("Enter lower range of interval: "))
upper_range = int(input("Enter upper range of interval: "))
print("The Armstrong numbers in given interval are:-")
for num in range(lower_range, upper_range + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp = temp // 10
    if num == sum:
        print(num)
