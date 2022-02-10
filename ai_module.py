from words import Words
import json

with open("simple.txt", "r") as file:
    slist = file.read().split("\n")
    print(slist)

with open("bow.json", "r") as file2:
    bdata = json.load(file2)
    print(bdata)

with open("vector.json", "r") as file3:
    vdata = json.load(file3)
    print(vdata)

def getdata(xarg):
    count = 0
    count2 = 0
    count3 = 0
    flag = 0
    answ = ""
    text = "try again.."
    nlist = []
    word = Words(xarg)
    w = word.load()
    for i in w:
        try:
            count = bdata.index(i)
            flag = 0
        except ValueError:
            flag = 1
        nlist.append(count)
    if flag != 1:
        for j in vdata:
            count2 = 0
            for i in nlist:
                if j[i] == 0:
                    count2 += 1
                    break
                else:
                    count2 += 1
                    if count2 == len(nlist):
                        answ = slist[count3]
                    else:
                        answ = text
        count3 += 1
    else:
        answ = text
    return answ
