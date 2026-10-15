# Lists II & For loops & Tuples
# J. Sun

# Using nested for loops to create 2D list
board = [['' for c in range(7)] for r  in range(6)]
print (board)

for row in board:
    
    for cell in row:
        
        print(cell, end=' ')

    print()
print()

grid = [[c for c in range(7)] for r  in range(6)]
print (grid)
print()

for row in grid:
    
    for cell in row:
    
        print(cell, end=' ')
    
    print()
print('---------------')
print('1 2 3 4 5 6 7')

