file_obj = open("test.txt")
for line in file_obj:
    print(line[0])

file_obj.close()
