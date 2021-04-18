# the list "walks" is already defined
res = 0
for dictionary in walks:
    res += dictionary['distance']

print(res // len(walks))
