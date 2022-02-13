from words import Words
import vector

llist = []
rlist = []
with open("data.txt", "r") as file:
        for line in file:
            if not line:
                continue
            else:
                left, right, *res = line.split(":")
                llist.append(left)
                rlist.append(right)
                varstring = " ".join(llist)
def getdata(xarg):
    answ = ""
    count = 0
    count2 = 0
    nlist = []
    ilist = []
    listvect = []
    listvect2 = []
    vect = vector.vector(llist)
    word = Words(xarg)
    w = word.load()
    instbow = Words(varstring)
    instb = instbow.load()
    for k in w:
        for i, x in enumerate(instb):
            if x == k:
                nlist.append(i)
    for j in vect:
        count = 0
        for i in nlist:
            if j[i] != 0:
                count += 1
        count2 += 1
        if count != 0:
            listvect.append(count)
            listvect2.append(count2-1)

    for i in listvect:
        y = i/len(nlist)
        ilist.append(y)

    if len(ilist) == 1:
        for i in listvect2:
            answ = rlist[i]
    else:
        for i in ilist:
            if i == max(ilist):
                m = ilist.index(i)
                v = listvect2[m]
                answ = rlist[v]
    return answ
