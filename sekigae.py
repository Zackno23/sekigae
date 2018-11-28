import random

all_list = []
with open("members.txt") as names:
    name_list = names.read().split("\n")


tf = False
# anotherlist = random.sample(TableA_list, len(TableA_list))
while True:
    tf = False
    while tf == False:
        anotherlist = random.sample(name_list, len(name_list))
        for i in range(len(name_list)):
            if i != len(name_list) - 1:
                nabor_list = [name_list[i - 1], name_list[i + 1]]
            else:
                nabor_list = [name_list[i - 1], name_list[0]]
            num = anotherlist.index(name_list[i])
            if num != len(name_list) - 1:
                another_nabor_list = [anotherlist[num - 1], anotherlist[num + 1]]
                if (nabor_list[0] in another_nabor_list) or (nabor_list[1] in another_nabor_list):
                    break
                else:
                    if i != len(name_list) - 1:
                        continue
                    else:
                        tf = True
                        break
            else:
                another_nabor_list = [anotherlist[num - 1], anotherlist[0]]
                if (nabor_list[0] in another_nabor_list) or (nabor_list[1] in another_nabor_list):
                    break
                else:
                    if i != len(name_list):
                        continue
                    else:
                        tf = True
                        break
        if not tf:
            continue
    Table_List_A = anotherlist[:6]
    Table_list_B = anotherlist[6:11]
    Table_List_C = anotherlist[11:]

    print(Table_List_A)
    print(Table_list_B)
    print(Table_List_C)

    str_another = "\n".join(anotherlist)
    with open("members.txt", "w") as file:
        file.write(str_another)
    question = input('席替えを続けますか?(y/n)')
    if question.lower() == "n":
        break
