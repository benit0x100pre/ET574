# Variables
# Handling the precision of floating-point numbers


#PI = 3.14159265359
#PI = 3.14
PI = 3

# use % operator
print('%.1f' % PI)
print('%.2f' % PI)
print('%.3f' % PI)
print()

# use format() method to format a specified value
print( "{:.6f} {:.2f} {:.3f}".format(0.123456789, 711, PI) )
print()

# f-string print with various levels of floating point precision
print(f"{PI:.1f}")
print(f"{PI:.2f}")
print(f"{PI:.3f}")
print(f"{PI:.4f}")
print(f"{PI:.5f}")
print()

# use round() for floating point precision
print(PI)
print(round(PI, 3))
print(round(PI))
print()

'''
Python’s built-in round() function can be useful, 
using it to set precision for financial or 
scientific calculations is not always reliable.
'''

