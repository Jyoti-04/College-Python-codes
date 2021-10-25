string = str(input("Enter a string: "))
string = string.casefold()
rev_str = reversed(string)
if list(string) == list(rev_str):
    print("The String is Palindrome.")
else:
    print("The String is not Palindrome.")