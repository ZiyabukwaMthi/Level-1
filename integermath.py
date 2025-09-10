# Ask the user to enter three different integers
X = int(input("Enter a integer X: "))
Y = int(input("Enter a integer Y: "))
Z = int(input("Enter a integer Z: "))

# The sum of all the numbers
Sum = X + Y + Z
print("Sum of all numbers is: ", Sum)

# The first number minus the second number
Difference = X - Y
print("The  first number minus the second number: ", Difference)

# The third number multiplied by the first number
Product = Z * X
print("The third number multiplied by the first number: ", Product)

# The sum of all three numbers divided by the third number
# 

if Z != 0:
    Qoutient = Sum / Z
    print("Sum of all three numbers divided by the third number: ", Qoutient)
else:
    print("Cannot divide by zero (third number is 0).")
