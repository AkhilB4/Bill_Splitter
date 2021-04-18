with open("test_file.txt", encoding="utf-16") as file_obj:
    lines_list = file_obj.readlines()

print(lines_list[0])
