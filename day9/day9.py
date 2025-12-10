# Day 9
import math
import sys

with open('input.txt') as f:
    coords = [(int(x.split(",")[0]),int(x.split(",")[1])) for x in f.readlines()]

# Part 1
# max_a = 0
# for xy in coords:
#     x,y = xy
#     for cxy in coords:
#         if cxy == xy:
#             continue
        
#         cx,cy = cxy

#         ca = (1+abs(x-cx))*(1+abs(y-cy))
#         if ca > max_a:
#             max_a = ca
# print(max_a)


# Part 2

def valid_rect(v1,v2,vs):
    if v1[0] > v2[0]:
        xmax = v1[0]
        xmin = v2[0]
    else:
        xmin = v1[0]
        xmax = v2[0]

    if v1[1] > v2[1]:
        ymax = v1[1]
        ymin = v2[1]
    else:
        ymin = v1[1]
        ymax = v2[1]

    valid = True
    for i in range(len(vs)):
        v = vs[i]
        vp = vs[i-1]
        
        if v[0] in range(xmin+1,xmax) and v[1] in range(ymin+1,ymax):
            valid = False
            break

        if (vp[0] >= xmax and v[0] <= xmin and v[1] in range(ymin+1,ymax)) or (vp[0]<=xmin and v[0] >= xmax and v[1] in range(ymin+1,ymax)) or (vp[1] >= ymax and v[1] <= ymin and v[0] in range(xmin+1,xmax)) or (vp[1] <= ymin and v[1] >= ymax and v[0] in range(xmin+1,xmax)):
            valid = False
            break
    return valid
            
            
max_a = 0
for i in range(len(coords)):
    xy = coords[i]
    for cxy in coords[i+1:]:
        if xy == cxy or not valid_rect(xy,cxy,coords):
            continue

        x,y = xy
        cx,cy = cxy
        ca = (1+abs(x-cx))*(1+abs(y-cy))
        if ca > max_a:
            max_a = ca

print(max_a)
