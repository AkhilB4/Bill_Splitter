import random

users = int(input("Enter the number of friends joining (including you):\n"))

print("Enter the name of every friend (including you), each on a new line:")

persons_list = []
for _ in range(users):
    persons_list.append(input())

random.seed()

total_amt = int(input("Enter the total bill value:\n"))
choice = input('Do you want to use the "Who is Lucky?" feature? Write Yes/No:\n')

if choice == "Yes":
    person = random.choice(persons_list)
    print(f"{person} is the lucky one!")
    try:
        money = round(total_amt / (users - 1), 2)
    except ZeroDivisionError:
        persons_dict = dict.fromkeys(persons_list, 0)
    else:
        persons_dict = dict.fromkeys(persons_list, money)
    persons_dict[person] = 0
    print(persons_dict)
else:
    print("No one is going to be lucky")
    try:
        money = round(total_amt / (users - 1), 2)
    except ZeroDivisionError:
        persons_dict = dict.fromkeys(persons_list, 0)
    else:
        persons_dict = dict.fromkeys(persons_list, money)
    print(persons_dict)
