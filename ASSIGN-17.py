def fib(number_of_term):
    counter = 0
    first = int(input("Enter first term: "))
    second = int(input("Enter second term: "))
    while counter <= number_of_term:
        print(first)
        temp = first + second
        first = second
        second = temp
        counter = counter + 1


fib(11)
