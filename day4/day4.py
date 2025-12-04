# Day four

with open("input.txt") as f:
    data = [[x for x in y.strip()] for y in f.readlines()]

# part 1
# accessible = 0
# l = len(data)
# w = len(data[0])
# for i in range(l):
#     for j in range(w):
#         if data[i][j] != "@":
#             continue
        
#         rolls = -1
#         if i > 0:
#             min_y = i-1
#         else:
#             min_y = i
#         if i < l-1:
#             max_y = i+2
#         else:
#             max_y = i+1

#         if j > 0:
#             min_x = j-1
#         else:
#             min_x = j
#         if j < w-1:
#             max_x = j+2
#         else:
#             max_x = j+1

#         for y in range(min_y,max_y):
#             for x in range(min_x,max_x):
#                 if data[y][x] == "@":
#                     rolls += 1

#         if rolls < 4:
#             accessible += 1

# print(accessible)

# Part 2
def count_rolls(data):
    count = 0
    for row in data:
        count += row.count("@")

    return count

def print_grid(data):
    for line in data:
        print("".join(line))

removed = 0
l = len(data)
w = len(data[0])

old_count = count_rolls(data)+1

while old_count > count_rolls(data):
    old_count = count_rolls(data)
    for i in range(l):
        for j in range(w):
            if data[i][j] != "@":
                continue

            rolls = -1
            if i > 0:
                min_y = i-1
            else:
                min_y = i
            if i < l-1:
                max_y = i+2
            else:
                max_y = i+1

            if j > 0:
                min_x = j-1
            else:
                min_x = j
            if j < w-1:
                max_x = j+2
            else:
                max_x = j+1

            for y in range(min_y,max_y):
                for x in range(min_x,max_x):
                    if data[y][x] == "@":
                        rolls += 1

            if rolls < 4:
                data[i][j] = "."
                removed += 1
            
print(removed)
