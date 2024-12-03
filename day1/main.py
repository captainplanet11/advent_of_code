file = open("input.txt", "r")
content = file.read()

floor = 0
for i in content:
    if i == '(':
        floor += 1
    else:
        floor -= 1
    
print(floor)

