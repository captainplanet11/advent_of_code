data = open("input.txt").read().splitlines()


feet_ribbon =  0 
for i in data:
    l, w, h = sorted(map(int, i.strip().split('x')))
    feet_ribbon += l*2 + w *2
    feet_ribbon += l*w*h
print(feet_ribbon)