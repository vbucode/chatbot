# make vector from data with text:template
# files line is userwrite:reply

from words import Words

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

def bow():
    instbow = Words(varstring)
    instb = instbow.load()
    return instb
def vector():
    klist = []
    vlist = []
    nlist = []
    instvect = Words(varstring)
    instv = instvect.load()
    for i in llist:
        insth = Words(i)
        w = insth.load()
        nlist.append(w)
    for i in range(len(nlist)):
        klist.append([0]*len(instv))
    for k in instv:
        for i in nlist:
            for j in i:
                if k == j:
                    klist[nlist.index(i)][instv.index(k)] = 1
    return klist

def reply():
    return rlist
