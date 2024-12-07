import time ## used for simple runtime calculation
"""
Read input
"""
inputpath="input.txt"
grid = []
with open(inputpath, 'r') as file:
    for line in file:
        grid.append([x for x in line.strip()])

"""
Symbols that indicate the start location of the guard
"""
start_symbols = ["^", "<", ">","v"] # Task 1

"""
Map of direction id's to direction vector 
"""
directions = { # Task 1
    0 : (0,-1), # Up
    1 : (1,0), # Right
    2 : (0,1), # Left
    3 : (-1,0) # Down
}

"""
Helper functions to 
- identify starting position
- check if the guard has gone beyond map borders
- check if a position is occupied by an obstacle
"""
def get_starting_position(): # Task 1
    starting_position = None
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] in start_symbols:
                starting_position = (x,y)
                return starting_position

def out_of_bounds(x : int,y : int) -> bool: # Task 1
    return x < 0 or x > len(grid[0])-1 or y < 0 or y > len(grid) - 1

def no_obstacle(x : int,y : int) -> bool: # Task 1
    return grid[y][x] != "#"

"""
Main loop Task 1
"""
def simulate_walk(start : tuple) -> None: # Task 1 & 2
    current_position = start
    curr_x = current_position[0]
    curr_y = current_position[1]
    curr_heading = 0
    path = set() # Track the set of unique grid-points visited by the guard
    states = set() # Track the set of states the guard has been in to identify loops
    loop = False
    left_the_map = False
    while(not loop and not left_the_map):
        ## Tracking the guards route
        if (curr_x, curr_y, curr_heading) in states: # Given its map, if the guard has been in this position, with the same heading, he will repeat his behaviour that led to this point, hence is in a loop.
            loop=True
        states.add((curr_x, curr_y, curr_heading))
        path.add((curr_x, curr_y))
        ## Calculate new location
        delta_x, delta_y = directions[curr_heading]
        new_x, new_y = curr_x + delta_x, curr_y + delta_y 
        ## Check if the new location
        if out_of_bounds(new_x, new_y): # is outside of map -> loop terminates, guard left the map
            curr_x, curr_y = (new_x, new_y)
            left_the_map = True
        elif no_obstacle(new_x, new_y): # is free -> its safe to change the guards location
            curr_x, curr_y = (new_x, new_y)
        else:
         curr_heading = (curr_heading + 1) % 4 # is occupied -> change heading and try again
    return loop, states, path, len(path)

"""
Main loop Task 1
"""
def simulate_walks(start):
    loop, _, path, _ = simulate_walk(start)
    if loop:
        raise Exception("The guard is already in a loop in the unaltered map")
    loop_counter = 0
    # Place obstacle only at those locations, which the guard would eventually visit in its default run
    for (node_x, node_y) in path: 
        elem = grid[node_y][node_x]
        if elem in start_symbols or elem == "#":
            continue
        grid[node_y][node_x] = "#"
        res, _, _, _ = simulate_walk(start)
        loop_counter += res
        grid[node_y][node_x] = "."
    return loop_counter

print("Starting with Task 1..")
start = get_starting_position()
st = time.time()
_, _, _, res1 = simulate_walk(start)
et = time.time()
print("Task 1:", res1, "(took " + str(et-st) + "s)")

print("Starting with Task 2..(may take some seconds)")
start = get_starting_position()
st = time.time()
res2 = simulate_walks(start)
et = time.time()
print("Task 2:", res2, "(took " + str(et-st) + "s)")
