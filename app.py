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
        global answ
        searchlist = []
        answ = ""
        ilist = []
        listvect = []
        tlist = []
        for i in llist:
            ll = Words(i)
            l = ll.load()
            tlist.append(l)
        ivect = WordVector(tlist)
        vect = ivect.load()
        word = Words(self.xarg)
        w = word.load()
        instb = ivect.bow()
        instlinetokenize = ivect.senttokenize()
        for k in w:
            for i, x in enumerate(instb):
                if x == k:
                    searchlist.append(i)

        if len(searchlist) != 0:
            # поиск в векторе и запись в формате [совпадение = 1:индекс в векторе]
            for j in vect:
                for i in searchlist:
                    if j[i] != 0:
                        listvect.append(vect.index(j))

            # проверка на присутствие в индексах вектора(предложений)
            c = Counter(listvect)
            v = (max(set(listvect), key=lambda x: listvect.count(x)))
            if len(instlinetokenize[v]) == c[v]:
                answ = rlist[(max(set(listvect), key=lambda x: listvect.count(x)))]

        if answ in tags:
            for i in tags:
                if i == answ:
                    for j in tags[i]:
                        answ = j["content"]

        return answ
