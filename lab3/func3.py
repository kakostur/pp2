def solve(numheads, numlegs):
    c = (numlegs-(2 * numheads)) / 2
    r = numheads - c
    return c, r

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)
