# Day 7

with open("input.txt") as f:
    rows = [x.strip() for x in f.readlines()]

# splits = 0
# beams = {rows[0].find("S")}

# for row in rows[1:]:
#     if "^" not in row:
#         continue 
#     for i in range(len(row)):
#         if row[i] == "^" and i in beams:
#             splits += 1
#             beams.remove(i)
#             beams.add(i-1)
#             beams.add(i+1)

# print(splits)

# Part 2
mem = {}

def run_timeline(r, c, grid):
    if (r,c) in mem:
        return mem[(r,c)]
    for k in range(r, len(grid)):
        row = grid[k]
        if "^" not in row:
            continue        
        if row[c] == "^":
            result = run_timeline(k+1,c-1,grid) + run_timeline(k+1,c+1,grid)
            mem[(r,c)] = result
            return result        
            
    mem[(r,c)] = 1
    return 1

start = rows[0].find("S")

print(run_timeline(0,start,rows))
