# Day three

with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

max_jolts = []

# Part 1
# for joltages in data:
#     max_jolt = 0
#     for i in range(len(joltages)):
#         for j in range(i+1,len(joltages)):
#             cj = int(joltages[i])*10+int(joltages[j])
#             if cj > max_jolt:
#                 max_jolt = cj
#     max_jolts.append(max_jolt)

# print(sum(max_jolts))

# part 2
for joltages in data:
    cmj = 0
    jolts = [int(x) for x in list(joltages)]
    n = 11
    while len(jolts) > 0 and n >= 0:
        mj = max(jolts[:len(jolts)-n])
        idx = jolts.index(mj)
        cmj += mj * pow(10,n)
        n -= 1
        jolts = jolts[idx+1:]

    max_jolts.append(cmj)

print(sum(max_jolts))
    

