from collections import Counter
from words import Words
from wordvector import WordVector

llist = []
rlist = []

with open("data.txt", "r") as file:
        for line in file:
            if not line:
                continue
            else:
                left, right, *res = line.split(":")
                llist.append(left)
                rlist.append(right.replace("\n", ""))

class App:
    def __init__(self, xarg):
        self.xarg = xarg
    def getdata(self):
        answ = ""
        searchlist = []
        ilist = []
        slist = []
        listvect = []
        instb = []
        dlist = []
        for i in llist:
            vw = Words(i)
            wvl = vw.load()
            dlist.append(wvl)
        ivect = WordVector(dlist)
        vect = ivect.load()
        word = Words(self.xarg)
        w = word.load()
        # bag of words
        for i in dlist:
            for j in i:
                instb.append(j)
        for k in w:
            for i, x in enumerate(instb):
                if x == k:
                    searchlist.append(i)

        if len(searchlist) != 0:
            for j in vect:
                for i in searchlist:
                    if j[i] != 0:
                        listvect.append(vect.index(j))

            c = Counter(listvect)
            v = (max(set(listvect), key=lambda x: listvect.count(x)))
            if len(dlist[v]) == c[v]:
                answ = rlist[(max(set(listvect), key=lambda x: listvect.count(x)))]

        return answ
