key_desired = int(input())

if key_desired not in squares:
    print("There is no such key")
else:
    print(squares.pop(key_desired))

print(squares)
