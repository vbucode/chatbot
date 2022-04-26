from collections import Counter
from words import Words
from wordvector import WordVector
import json

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

with open("tags.json", "r") as file2:
    tags = json.load(file2)

class App:
    def __init__(self, xarg):
        self.xarg = xarg
        
    def getdata(self):
        answ = ""
        searchlist = []
        ilist = []
        listvect = []
        dlist = []
        for i in llist:
            vw = Words(i)
            wvl = vw.load()
            dlist.append(wvl)
        ivect = WordVector(dlist)
        vect = ivect.load()
        word = Words(self.xarg)
        w = word.load()
        instb = ivect.bow()
        for k in w:
            for i, x in enumerate(instb):
                if x == k:
                    searchlist.append(i)

        if len(searchlist) != 0:
            for j in vect:
                for i in searchlist:
                    if j[i] != 0:
                        listvect.append(vect.index(j))

            for i in listvect:
                ilist.append(i)
                c = Counter(ilist)
                v = (max(set(ilist), key=lambda x: ilist.count(x)))
                if len(dlist[v]) == c[v]:
                    answ = rlist[(max(set(ilist), key=lambda x: ilist.count(x)))]

        if answ in tags:
            for i in tags:
                if i == answ:
                    for j in tags[i]:
                        answ = j["content"]
    
        return answ
