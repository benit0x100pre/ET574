# Lists II & For loops & Tuples
# J. Sun

#create 2D lists
grid_zeros = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

grid_strings = [
    ['ant', 'bee', 'cat', 'dog'],
    ['elephant', 'fox', 'giraffe', 'horse']
]

grid_integers = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]


grid_letters = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
#To get specific rows or ranges of rows, you can slice the outer list:
row_slice = grid_letters[:2] # To get the first two rows:
print(row_slice)  # Output: [['A', 'B', 'C'], ['D', 'E', 'F']]

last_row = grid_letters[-1:] # To get the last row:
print(last_row)  # Output: [['G', 'H', 'I']]

#Column Slicing:
#If you want to get specific columns, you'll have to use a loop or list comprehension since 2D lists are lists of lists:
#To get the first column (i.e., ['A', 'D', 'G']):
first_column = [row[0] for row in grid_letters]
print(first_column)  # Output: ['A', 'D', 'G']

second_column = [row[1] for row in grid_letters]
print(second_column)  # Output: ['B', 'E', 'H']

#Slicing Both Rows and Columns:
#To get the first two rows and first two columns:
row_col_slice = [row[:2] for row in grid_letters[:2]]
print(row_col_slice)  # Output: [['A', 'B'], ['D', 'E']]

#To get the last two columns from the last two rows:
last_two = [row[1:] for row in grid_letters[-2:]]
print(last_two)  # Output: [['E', 'F'], ['H', 'I']]








print("slicing", grid_letters[1:-1])
board = [['O' for c in range(7)] for r  in range(6)]
print (board)

grid = [[c for c in range(7)] for r  in range(6)]
print (grid)

print("slicing", grid[1:-1])




