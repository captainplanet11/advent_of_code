data = open("input.txt").read()
floor = 0


for position, char in enumerate(data, start=1):
    floor += 1 if char =='(' else - 1
    if floor == -1:
        print(position)
    

