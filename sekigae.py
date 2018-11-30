import random

from shuffle import shuffle

all_list = []
with open("members.txt") as names:
    name_list = names.read().split("\n")


tf = False
while True:
    tf = False
    table_list = shuffle(name_list, tf)

    print(table_list[:6], table_list[6:11], table_list[11:])

    str_another = "\n".join(table_list)
    with open("members.txt", "w") as file:
        file.write(str_another)
    print('本日の主役:', random.choice(name_list))
    question = input('席替えを続けますか?(y/n)')
    if question.lower() == "n":
        break
