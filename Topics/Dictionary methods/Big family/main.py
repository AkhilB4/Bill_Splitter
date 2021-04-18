# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

first_family.update(second_family)
big_family = first_family
print(big_family)
