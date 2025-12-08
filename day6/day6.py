# Day six
import math

# part 1
# with open("input.txt") as f:
#     rows = [x.strip() for x in f.readlines()]

# row = rows[0]

# n_r = len(rows)
# rls = []
# for row in rows:
#     while "  " in row:
#         row = row.replace("  "," ")

#     rl = row.split(" ")
#     rls.append(rl)

# ans = 0
# for i in range(len(rls[0])):
#     op = rls[n_r-1][i]
#     nums = []
#     for j in range(n_r-1):
#         nums.append(int(rls[j][i]))

#     if op == '+':
#         ans += sum(nums)
#     else:
#         ans += math.prod(nums)

# print(ans)
    
with open("input.txt") as f:
    rows = [x[:-1] for x in f.readlines()] # Don't wanna lose any trailing spaces

break_cols = []   

for i in range(len(rows[0])):
    non_space = False
    for j in range(len(rows)):
        if rows[j][i] != " ":
            non_space = True
            break
    if not non_space:
        break_cols.append(i)

split_rows = [[] for row in rows]
    
for i in range(len(break_cols)+1):
    if i == 0:
        start = 0
    else:
        start = break_cols[i-1]+1

    if i == len(break_cols):
        end = len(row)
    else:
        end = break_cols[i]
        
    for j in range(len(rows)):
        split_rows[j].append(rows[j][start:end])

ops = [x.strip() for x in split_rows[-1]]
answers = []
for x in range(len(split_rows[0])):
    n = len(split_rows[0][x])
    nums = []
    for i in range(n):
        cn = ""
        for j in range(len(split_rows)-1):
            cn += split_rows[j][x][i]
        nums.append(int(cn.strip()))

    if ops[x] == "+":
        answers.append(sum(nums))
    else:
        answers.append(math.prod(nums))

print(sum(answers))
        
