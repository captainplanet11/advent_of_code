# import numpy as np
data = open("input.txt").read().strip()

# print(data)
#starting position 
x,y = 0,0
visited_houses = set()
visited_houses.add((x,y))

for move in data:
    if move == '>':  # Move east
        x += 1
    elif move == '<':  # Move west
        x -= 1
    elif move == '^':  # Move north
        y += 1
    elif move == 'v':  # Move south
        y -= 1

    visited_houses.add((x,y))

print(len(visited_houses))


