import random

all_list = []
with open("members.txt") as names:
    name_list = names.read().split("\n")
TableA_list = random.sample(name_list, 6)
for name in TableA_list:
    name_list.remove(name)
TableB_list = random.sample(name_list, 5)
for name in TableB_list:
    name_list.remove(name)
TableC_list = name_list
print(TableA_list)
all_list = [TableA_list, TableB_list, TableC_list]

tf = False
# anotherlist = random.sample(TableA_list, len(TableA_list))

while tf == False:
    anotherlist = random.sample(TableA_list, len(TableA_list))
    for i in range(len(TableA_list)):
        if i != 5:
            nabor_list = [TableA_list[i - 1], TableA_list[i + 1]]
        else:
            nabor_list = [TableA_list[i - 1], TableA_list[0]]
        num = anotherlist.index(TableA_list[i])
        if num != 5:
            another_nabor_list = [anotherlist[num - 1], anotherlist[num + 1]]
            if (nabor_list[0] in another_nabor_list) or (nabor_list[1] in another_nabor_list):
                break
            else:
                if i != 5:
                    continue
                else:
                    print(anotherlist)
                    tf = True
                    break
        else:
            another_nabor_list = [anotherlist[num - 1], anotherlist[0]]
            if (nabor_list[0] in another_nabor_list) or (nabor_list[1] in another_nabor_list):
                break
            else:
                if i != 5:
                    continue
                else:
                    print(anotherlist)
                    tf = True
                    break
    if not tf:
        continue
'''
'''
# for i in range(len(TableA_list)):
#     nabor_dict = {TableA_list[i]:[TableA_list[i-1],TableA_list[i+1]]}
#
