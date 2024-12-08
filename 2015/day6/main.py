instructions = open("input.txt").read().splitlines()

def process_instructions(instructions):
    grid = [[False] * 1000 for _ in range(1000)]
    
    def apply_instruction(action, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "turn on":
                    grid[x][y] = True  
                elif action == "turn off":
                    grid[x][y] = False 
                elif action == "toggle":
                    grid[x][y] = not grid[x][y] 
    
    for instruction in instructions:
        parts = instruction.split()
        if parts[0] == "toggle":
            action = "toggle"
            start = parts[1]
            end = parts[3]
        else:  
            action = " ".join(parts[:2])
            start = parts[2]
            end = parts[4]
        
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        
        apply_instruction(action, x1, y1, x2, y2)
    
    lights_on = sum(row.count(True) for row in grid)
    return lights_on



lights_on = process_instructions(instructions)
print(lights_on)
