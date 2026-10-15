# Variables: Strings
# String literals


# string using double quotes
greet = "Hi there"
print("Hi there")
print(greet)

# print a blank line
print("")
print('')
print()

# string using single quotes
address = '5th Avenue'
print('5th Avenue')
print(address)
print()

# single quotation used as an apostrophe
#print('This is a string with a 'quotation' in it.')  #invalid syntax
print("This is a string with a 'quotation' in it.")
print('This is a string with a \'quotation\' in it.')
print()

# tripe quote strings enable printing of ' and " characters in the same string
txt = '''1) This is a string
with a 'single quotation' and
a "double quotation" in it.\n'''
print(txt)

print("""2) This is a string
with a 'single quotation'
and a "double quotation" in it.\n""")

print('''
3) This is a string
with a 'single quotation'
and a "double quotation" in it.\n
''')


# use backslash to split a long statement
print('4) This is a string\n\
with multiple lines\
to be displayed.\n')

newTxt = '5) This is a string\n\
with multiple lines \
to be displayed.\n'
print (newTxt)


# use (+) to split a long statement
newTxt = ('6) This is a string\n'+
'with multiple lines' +
'to be displayed.\n')
print (newTxt)