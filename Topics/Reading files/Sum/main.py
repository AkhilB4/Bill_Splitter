file_obj = open("sums.txt")
for line in file_obj:
    a, b = map(int, line.split())
    print(a + b)

file_obj.close()
