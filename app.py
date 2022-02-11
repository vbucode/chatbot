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
    answ = ""
    reply = "try again.."
    nlist = []
    listvect = []
    listvect2 = []
    rlist = []
    word = Words(xarg)
    w = word.load()
    for k in w:
        for i, x in enumerate(bdata):
            if x == k:
                nlist.append(i)
    print(nlist)
    for j in vdata:
        count = 0
        for i in nlist:
            if j[i] != 0:
                count += 1
        count2 += 1
        if count != 0:
            listvect.append(count)
            listvect2.append(count2-1)
    print(listvect)
    print(listvect2)

    for i in listvect:
        y = i/len(nlist)
        rlist.append(y)
    print(rlist)
    if len(rlist) == 1:
        for i in listvect2:
            answ = slist[i]
    else:
        for i in rlist:
            if i == max(rlist):
                m = rlist.index(i)
                v = listvect2[m]
                print(v)
                answ = slist[v]
    
    return answ
