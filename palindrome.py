''' checking whether the given string is palindrome or not '''
string = input("enter the string: ")
str_rev = ''.join(reversed(string));
if str_rev == string:
    print("palindrome ");
else:
    print("not a palindrome ");