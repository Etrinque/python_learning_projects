"""Conway Game of Life"""

import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Creat list of list for cells:
next_cells = []
for x in range(WIDTH):
    column = []                         # create new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')          # Add Living Cell.
        else:
            column.append(' ')          # Add Dead Cell
    next_cells.append(column)           # List of Column Lists

while True:                             # Main program loop
    print('-----\n-----\n-----\n-----\n-----\n')                 # Separate step with newlines
    current_cells = copy.deepcopy(next_cells) # Print Current_cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end=' ')
        print()                         # Calculate next step cells on current step cells
    for x in range(WIDTH):
                                        # Ensures cell is within 0 and (arg - 1)
        for y in range(HEIGHT):
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT
                                        # Count neighbors living, Top left neighbor alive etc. etc.
            neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                neighbors += 1
            if current_cells[x][above_coord] == '#':
                neighbors += 1
            if current_cells[right_coord][above_coord] == '#':
                neighbors += 1
            if current_cells[left_coord][y] == '#':
                neighbors += 1
            if current_cells[right_coord][y] == '#':
                neighbors += 1
            if current_cells[left_coord][below_coord] == '#':
                neighbors += 1
            if current_cells[x][below_coord] == '#':
                neighbors += 1
            if current_cells[right_coord][below_coord] == '#':
                neighbors += 1
                                        # Setting cells based on Conways Rules
            if current_cells[x][y] == '#' and (neighbors == 2 or neighbors == 3):
                next_cells[x][y] = '#'
                                        # w/ 2/3 neighbors stays alive
            elif current_cells[x][y] == ' ' and neighbors == 3:
                next_cells[x][y] = '#'
                                        # Dead cells w/ 3 neighbors become alive
            else:
                next_cells[x][y] = ' '
                                        # Everyhting else dies
    time.sleep(1)
                                        # Add 1 second pause