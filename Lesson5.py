a = int(input("enter first number"))
b = int(input("enter second number"))
try:
    print(a*b)
except TypeError:
    print("invalid numbers type")