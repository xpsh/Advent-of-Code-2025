
with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

zeros = 0
c = 50

# Part 1

# for line in data:
#     dir = line[0]
#     rots = int(line[1:])

#     if dir == 'R':
#         c = (c+rots)%100
#     else:
#         c = (c-rots)%100

#     if c == 0:
#         zeros += 1

# print(zeros)
    
# Part 2
for line in data:
    dir = line[0]
    rots = int(line[1:])

    if dir == 'R':
        tc = c+rots
        zeros += tc//100
        c = (c+rots)%100
    else:
        tc = c-rots
        if tc <= 0:
            if c != 0:
                zeros += -1*tc//100+1
            else:
                zeros += -1*tc//100
            
        c = (c-rots)%100

print(zeros)
