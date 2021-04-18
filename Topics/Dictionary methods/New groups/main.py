groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
group_num = int(input())

group_dict = {}
for i in range(group_num):
    group_dict[groups[i]] = int(input())

for i in range(group_num, len(groups)):
    group_dict[groups[i]] = None

print(group_dict)
