import random


def shuffle(name_list, tf):
    while not tf:
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
    return anotherlist
