from collections import Counter
from words import Words
import wordvector
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

def getdata(xarg):
    answ = ""
    searchlist = []
    ilist = []
    listvect = []
    vect = wordvector.vector(llist, tfidf = 0)
    word = Words(xarg)
    w = word.load()
    instb = wordvector.bow()
    instlinetokenize = wordvector.linetokenize()
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
