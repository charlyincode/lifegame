import os
import copy
import time

def create_grid(rows,cols):
    grid=[]
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(0)
        grid.append(row)
    return grid

def place_object(grid,pattern):
    for x, y in pattern:
        grid[x][y] = 1

def display(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    grid_displayed = ''
    for row in grid:
        line=""
        for cell in row:
            if cell:
                line += "■"
            else:
                line += "."
        line += '\n'
        grid_displayed += line
    print(grid_displayed)

def count_neighbors(grid,x,y):
    count = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if( i == x and j == y) or i < 0 or j < 0 or i >= len(grid) or j>= len(grid[0]):
                continue
            count += grid[i][j]
    return count

def update(grid):
    new_grid = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y]:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def run_game():
    grid = create_grid(10,10)
    blinker_init = [(4,5),(5,5),(6,5)]
    place_object(grid,blinker_init)
    print("Jeu de la vie - Appuyer sur Ctrl+c pour quitter")
    time.sleep(2)
    while True:
        display(grid)
        grid = update(grid)
        time.sleep(0.5)

run_game()