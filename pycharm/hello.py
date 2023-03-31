def add(a, b):
    return sum(a, b)
def mul(a, b):
    return multi(a, b)
def sub(a, b):
    return subs(a, b)
def div(a, b):
    return divid(a, b)
a = int(input("Enter a number to add/sub/multi/div: "))
b = int(input("Enter a number to add/sub/multi/div: "))
sum = a + b
multi = a * b
subs = a - b
divid = a / b
print("The sum of a and b is :",sum)
print("The subtraction of a and b is :",subs)
print("The divide of a and b is :",divid)
print('The multiplication of a and b is :',multi)