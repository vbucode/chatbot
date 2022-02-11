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
    reply = ""
    text = "try again.."
    nlist = []
    xlist = []
    listvect = []
    listvect2 = []
    ylist = []
    rlist = []
    word = Words(xarg)
    w = word.load()
    for k in w:
        for i, x in enumerate(bdata):
            if x == k:
                nlist.append(i)

    for j in vdata:
        count = 0
        for i in nlist:
            if j[i] != 0:
                count += 1
        count2 += 1
        listvect.append(count)
        if j[i] != 0:
            listvect2.append(count2)
    print(listvect)
    print(listvect2)

    for i in listvect:
        if i != 0:
            ylist.append(i)

    for x in ylist:
        y = x/len(nlist)
        print(int(y))
        rlist.append(int(y))
        if y == 1:
            reply = slist[int(y)-1]
        else:
            pass
    
    return reply
