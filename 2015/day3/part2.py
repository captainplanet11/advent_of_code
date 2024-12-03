
data = open("input.txt").read().strip()


santa_pos = (0, 0)
robo_pos = (0, 0)
visited_houses = set()

# Both start at the same location
visited_houses.add(santa_pos)

# Alternate turns between Santa and Robo-Santa
for i, move in enumerate(data):
    if i % 2 == 0:  # Santa's turn
        x, y = santa_pos
        if move == '>':
            santa_pos = (x + 1, y)
        elif move == '<':
            santa_pos = (x - 1, y)
        elif move == '^':
            santa_pos = (x, y + 1)
        elif move == 'v':
            santa_pos = (x, y - 1)
        visited_houses.add(santa_pos)
    else:  
        x, y = robo_pos
        if move == '>':
            robo_pos = (x + 1, y)
        elif move == '<':
            robo_pos = (x - 1, y)
        elif move == '^':
            robo_pos = (x, y + 1)
        elif move == 'v':
            robo_pos = (x, y - 1)
        visited_houses.add(robo_pos)

print(len(visited_houses))