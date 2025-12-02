# Day two

with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

ranges = data[0].split(",")

invalid_ids = []

# Part 1
# for raw_range in ranges:
#     start, end= [int(x) for x in raw_range.split('-')]
#     for i in range(start,end+1):
#         str_i = str(i)
#         str_length = len(str_i)
#         if str_length%2:
#             continue
#         else:
#             front = str_i[:str_length//2]
#             back = str_i[str_length//2:]
#             if front==back:
#                 invalid_ids.append(i)

# print(sum(invalid_ids))

# part 2
for raw_range in ranges:
    start, end= [int(x) for x in raw_range.split('-')]
    for i in range(start,end+1):
        str_i = str(i)
        str_length = len(str_i)
        for m in range(1,str_length//2+1):
            if str_length%m:
                continue
            else:
                part = str_i[:m]
                temp_str = str_i.replace(part,'')
                if not len(temp_str):
                    invalid_ids.append(i)
                    break
                
print(sum(invalid_ids))
