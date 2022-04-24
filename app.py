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
                rlist.append(righе.replace("\n", ""))

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
        ivect = WordVector(llist)
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
            # поиск в векторе изапись в формате [совпадение:индекс в векторе]
            for j in vect:
                for i in searchlist:
                    if j[i] != 0:
                        listvect.append([1,vect.index(j)])

            # проверка на присутствие в индексах вектора(предложений)
            if len(listvect) == 1:
                for i in listvect:
                    if len(listvect) == len(instlinetokenize[i[1]]):
                        answ = rlist[i[1]]

            else:
                for i in listvect:
                    ilist.append(i[1])
                    c = Counter(ilist)
                    v = (max(set(ilist), key=lambda x: ilist.count(x)))
                    if len(instlinetokenize[v]) == c[v]:
                        answ = rlist[(max(set(ilist), key=lambda x: ilist.count(x)))]

        if answ in tags:
            for i in tags:
                if i == answ:
                    for j in tags[i]:
                        answ = j["content"]
    
        return answ
