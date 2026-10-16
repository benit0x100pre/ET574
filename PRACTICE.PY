#decision lab6 - 3 lists and case insensitive
# '''
# 1) name list
# 2) request your username
# 3) change namelist to one case: uppercase
# 4) if your username in uppercase is in the list


# '''


# usernames = ['admin', 'tom', 'jerry', 'dora', 'GEOGRE']
# name = input("enter your username: ")


# #list comprehension PRACTICE THIS AT HOME
# currentlist = [i.upper() for i in usernames]
# print(currentlist)




# if name.upper() in currentlist:
#     print(f'sorry {name}, that name is taken.\ncurrent user: {username}')
# else:
#     usernames.append(name)
#     print(f'great, {name} is still available.\nUpdated users: {usernames}')




#5 practice run
#a, b, c = 2, 3, 0
#print((a == b) and ((a * a < b * b) or (b < a) and (2 *a < b)))


# let = input("Enter A, B or C: \n")
# let = let.upper()
# if (let == 'A' or let == 'a'):
#     print('\nA, my name is Alice.')
# elif (let == 'B'):
#     print('\nTo be, or not to be.')
# elif (let == 'C'):
#     print('\nOh, say, can you see.')
# else:
#     print('\nInvalid letter.')






# #lab 7 - 1 REVIEW FOR LOOP
# print('for loop')
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end = " ")
# print()




# print('while loop')
# n = 1
# while n <= 101:
#     if n % 2 == 0:
#         print(n, end =" ")
#     n+=1






#4
print('for loop')
for i in range(9, 0, -1):
    print(i)
else:
    print("happy new year")


print('while loop')
x = 9
while x > 0:
    print(x)
    x-=1
#8-- sentienl while loop without function
lst = []
n = 1
try:
    while n != 0:
        n = eval(input('enter a number or a 8 to stop: '))
        if n != 0:
            lst.append(n)
    else:
                print(f'sum = {sum(lst)} \nAverage = {sum(lst)/len(lst):.2f}')
                print('numbers(s) entered: ')
                for i in lst:
                        print(i, end =' ')
except:
    print('invalid input')



