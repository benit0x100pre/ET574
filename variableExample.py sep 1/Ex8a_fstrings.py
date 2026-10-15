# Variables
# Using f-strings

fruit1 = "apples"
fruit2 = "pears"
qty = 7

# f-strings are used to format string content
print(f"1) I want to buy {qty} "
f"{fruit1} and {fruit2}.\n")
print(f"2) Hi my favorite number is {qty}!\n")

# f-strings can be used upon variables
txt = f"3) Hi, do you want to buy {qty} {fruit1}?\n"
print(txt)

# f-strings can span multiple lines if parenthesis are used
txt = (f"4) {fruit1.title()}"
f" and {fruit2} are delicious.\n")
print(txt)

txt = (f"5) {fruit1.title()}" +
f" and {fruit2} are delicious.\n")
print(txt)

txt = (f"6) {fruit1.title()} \
and {fruit2} are delicious.\n")
print(txt)

shoppingList = f"7) I want to buy {qty} {fruit1} and {fruit2}.\n"
print(shoppingList)
print(f"8) I want to buy {qty} {fruit1} and {fruit2}.\n")
print()

