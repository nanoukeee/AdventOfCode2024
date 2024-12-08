import time

"""
Read input
"""
input_path=""
antenna_map = {}
grid = []
with open(input_path,'r') as file:
    for y, line in enumerate(file):
        grid.append([x for x in line.strip()])
        for x, letter in enumerate(line.strip()):
            if letter == "." or letter == "#":
                continue
            elif letter in antenna_map:
                antenna_map[letter].add((x,y))
            else:
                antenna_map[letter] = set([(x,y)])

"""
Helper functions and globals
"""
vert_lim_idx = len(grid)-1
horiz_lim_idx = len(grid[0])-1
max_dist = max(vert_lim_idx, horiz_lim_idx)

def out_of_bounds(x : int, y : int) -> bool:
    return x < 0 or x > horiz_lim_idx or y < 0 or y > vert_lim_idx

def calculate_new_position(curr_x : int, curr_y : int, diff_x : int, diff_y : int, factor : int) -> tuple:
    return (curr_x + factor * diff_x, curr_y + factor * diff_y)

"""
Task 1
"""
def calculate_antinode_locations() -> int:
    antinode_locations = set()
    for type in antenna_map.keys():
        for pos in antenna_map[type]:
            for neighb in antenna_map[type]:
                if pos != neighb:
                    diff_x, diff_y = neighb[0] - pos[0], neighb[1] - pos[1]
                    antinode_x, antinode_y = calculate_new_position(pos[0], pos[1], diff_x, diff_y, 2) 
                    if not out_of_bounds(antinode_x, antinode_y):
                        antinode_locations.add((antinode_x, antinode_y))
    return len(antinode_locations)

"""
Task 2
"""
def calculate_antinode_locations_2() -> int:
    antinode_locations = set()
    for type in antenna_map.keys():
        for pos in antenna_map[type]:
            for neighb in antenna_map[type]:
                if pos != neighb:
                    diff_x, diff_y = neighb[0] - pos[0], neighb[1] - pos[1]
                    for factor in range(0, max_dist):
                        antinode_x, antinode_y = calculate_new_position(pos[0], pos[1], diff_x, diff_y, factor) 
                        if not out_of_bounds(antinode_x, antinode_y):
                            antinode_locations.add((antinode_x, antinode_y))
    return len(antinode_locations)

st = time.time()
res = calculate_antinode_locations()
et = time.time()
print("Task 1:", res ,"(took " + str(et-st) + ")")

st = time.time()
res = calculate_antinode_locations_2()
et = time.time()
print("Task 2:", res ,"(took " + str(et-st) + ")")

