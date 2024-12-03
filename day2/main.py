data = open("input.txt").read().splitlines()
# formula = 2*l*w + 2*w*h + 2*h*l

prism = 0
for i in data:
    l,w,h = map(int,i.strip().split('x'))
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    extra_paper = min(l * w, w * h, h * l)
    prism += surface_area
    prism += extra_paper

print(prism)