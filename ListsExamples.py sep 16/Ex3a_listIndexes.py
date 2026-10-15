# Intro to lists
# List indexes

# print individual elements of the list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0])  # list indexes start at 0, this is the first element
print(nums[1])
print(nums[3])
print(nums[4])
print(nums[5])
print(nums[6])
print(nums[7])
print(nums[8])
print(nums[9])
print(nums)
print()

#Compute the sum of first two numbers using the indexing to reference numbers in the list.
print('Sum =', nums[0] + nums[1])

#Compute the product of last two numbers using the indexing to reference numbers in the list.
print('Product =', nums[-1] * nums[-2])
print()


#--------------------------------
# negative indexing
grades = ['A', 'B', 'C', 'D', 'F']

#use negative indexing to reference each number in the list
print(grades[-1], grades[-2], grades[-3], grades[-4], grades[-5])
print()

#use negative one to print the list from the end to the starting
print(grades[::-1])   # list indexes ends at -1, this is the last element
print()

#use built-in function to print the temorary reversed list
print(sorted(grades, reverse = True))
print()

#use list method to sort the list permanently
grades.sort(reverse=True)
print(grades)
print()
