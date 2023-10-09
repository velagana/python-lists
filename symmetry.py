''' checking whether the given string is palindrome and symetrical or not '''
string = input("enter the string: ")
str_rev = ''.join(reversed(string))
if string == str_rev:
    print("The string is palindrome: ")
else:
    print("Not a palindrome :")
string1 = string[:len(string)//2]
string2 = string[-(len(string))//2]
if string1 == string2:
    print("The string is symetrical: ")
else:
    print("The string is not symmetrical : ")
