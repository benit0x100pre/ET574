# Variables
# Using built-in functions with numbers

# assignment of a single variable a
a = -10
print(a)

# simultaneous assignment of two variables, x and y
x,y = 2,3
print(x)
print(y)

# use built-in functions
print(abs(a))
print(bool(0))
print(pow(x, y))
print(round(3.1415926535897932, 6))

#round() is fine for basic use
#Not ideal for high precision or consistent formatting 
#Examples
print(round(2.675, 1))# It prints 2.7
print(round(2.678, 2))# You’d expect 2.68, but it prints 2.67
print(round(2.675, 4))# You’d expect 2.6750, but it prints 2.675

print(round(1.5))  # 2
print(round(2.5))  # 2   ← not 3!

value = 1.9999
print(round(value, 2))   # 2.0  ← not 2.00!

#Better using f-strings or format() for displaying fixed decimals
print(f"{value:.2f}")    # always shows 2 decimal places: 2.00
print('{:.2f}'.format(value))
