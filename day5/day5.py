# Day four

with open("input.txt") as f:
    data = f.read()

raw_ranges, ids = data.split("\n\n")
raw_ranges = [x.strip() for x in raw_ranges.strip().split("\n")]
ids = [int(x.strip()) for x in ids.strip().split("\n")]
ranges = [(int(x.split("-")[0]),int(x.split("-")[1])) for x in raw_ranges]

# Part 1
# goodcount = 0
# for n in ids:
#     for r in ranges:
#         if n >= r[0] and n <= r[1]:
#             goodcount += 1
#             break

# print(goodcount)


# Part 2
old_ranges = [x for x in ranges]
new_ranges = []

while True:
    for i in range(len(old_ranges)):
        r = old_ranges[i]
        added = False
        for j in range(len(new_ranges)):
            if j == i:
                continue
            nr = new_ranges[j]
            if r[0] >= nr[0] and r[0] <= nr[1] and r[1] >= nr[1]:
                new_ranges[j] = (nr[0],r[1])
                added = True
                break
            elif r[1] >= nr[0] and r[1] <= nr[1] and r[0] <= nr[0]:
                new_ranges[j] = (r[0],nr[1])
                added = True
                break
            elif r[0] <= nr[0] and r[1] >= nr[1]:
                new_ranges[j] = r
                added = True
                break
            elif r[0] >= nr[0] and r[1] <= nr[1]:
                new_ranges[j] = nr
                added = True
                break
        if not added:
            new_ranges.append(r)
    if len(new_ranges) < len(old_ranges):
        old_ranges = [x for x in new_ranges]
        new_ranges = []
        
    else:
        break
    
goodcount = 0
for r in new_ranges:
    goodcount += (r[1] - r[0] + 1)

print(goodcount)
        
