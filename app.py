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
def getdata(xarg):
    answ = ""
    count = 0
    count2 = 0
    searchlist = []
    ilist = []
    listvect = []
    listvect2 = []
    vect = vector.vector(llist, tf = 0)
    word = Words(xarg)
    w = word.load()
    instb = vector.bow()
    for k in w:
        for i, x in enumerate(instb):
            if x == k:
                searchlist.append(i)
    if len(searchlist) != 0:
        for j in vect:
            count = 0
            for i in searchlist:
                if j[i] != 0:
                    count += 1
                    count2 += 1
                    if count != 0:
                        listvect.append(count)
                        listvect.append(count2-1)
                        listvect2.append(listvect)
        if len(listvect2) == 1:
            for i in listvect2:
                answ = rlist[i[1]]
        else:
            for i in listvect2:
                for j in i:
                    if j[0]:
                        x = j[0]/len(searchlist)
                        ilist.append(x)
            if i == max(ilist):
                m = ilist.index(i)
                v = listvect2[m]
                answ = rlist[v]

    return answ
