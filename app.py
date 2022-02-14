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
    searchlist = []
    ilist = []
    listvect = []
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
            for i in searchlist:
                if j[i] != 0:
                    listvect.append([1,vect.index(j)])
        if len(listvect) == 1:
            for i in listvect:
                answ = rlist[i[1]]
        else:
            for i in listvect:
                ilist.append(i[1])
            for i in ilist:
                if i == max(ilist):
                    answ = rlist[i]

    return answ
