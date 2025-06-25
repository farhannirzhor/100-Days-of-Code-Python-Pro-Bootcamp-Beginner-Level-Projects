a = int (input("Enter first number: "))

b = int (input("Enter second number: "))

c = int (input("Enter third number: "))

if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
elif c > a and c > b:
    print("The largest number is:", c)
else:
        print("There is no largest number, at least two numbers are equal.")   