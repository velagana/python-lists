'''Count occurrences of an element in a list'''
list = [ 1,2,3,4,1,2,3,4,5,6,1,7,2,3]
count = 0
n = int(input("enter the value of n: "))
for i in list:
    if i == n:
        count = count+1
    print(count)
    