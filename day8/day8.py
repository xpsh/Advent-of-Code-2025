# Day 8
import math
import sys

def dist(a,b):
    return math.sqrt(pow((a[0]-b[0]),2) + pow((a[1]-b[1]),2) + pow((a[2]-b[2]),2))

with open("input.txt") as f:
    juncts = [(int(x.strip().split(",")[0]),int(x.strip().split(",")[1]),int(x.strip().split(",")[2])) for x in f.readlines()]

dm = {}

for i in range(len(juncts)):
    junct1 = juncts[i]
    for j in range(len(juncts)):
        junct2 = juncts[j]
        if i == j:
            continue
        else:
            d = dist(junct1,junct2)
            dm[d] = (junct1,junct2)

ds = list(dm.keys())
ds.sort()
circuits = [{j} for j in juncts]

# for p in range(1000):
#     d = ds[p]
#     j1,j2 =  dm[d]
#     in_c1 = False
#     c1 = None
#     in_c2 = False
#     c2 = None
#     for c in circuits:
#         if j1 in c:
#             in_c1 = True
#             c1 = c
#         if j2 in c:
#             in_c2 = True
#             c2 = c

#     if in_c1 and in_c2:
#         if c1 == c2:
#             continue
#         else:            
#             for nj in c2:
#                 c1.add(nj)
#             circuits.remove(c2)
#     elif in_c1:
#         c1.add(j2)
#     elif in_c2:
#         c2.add(j1)
#     else:
#         circuits.append({j1,j2})

             
# sizes = [len(x) for x in circuits]
# sizes.sort(reverse = True)
# print(sizes)
# print(sum(sizes))

# print(f"Part 1: {sizes[0]*sizes[1]*sizes[2]}")

# Part 2
p = 0
while len(circuits) > 1:
    d = ds[p]
    p += 1
    j1,j2 =  dm[d]
    c1 = None
    c2 = None
    for c in circuits:
        if j1 in c:
            c1 = c
        if j2 in c:
            c2 = c
            
    if c1 == c2:
        continue
    else:
        for nj in c2:
            c1.add(nj)
        circuits.remove(c2)
    
last_x = j1[0]*j2[0]

print(last_x)
