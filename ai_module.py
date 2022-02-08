from words import Words
import json
answ = ""
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
    global answ
    word = Words(xarg)
    w = word.load()
    posfunc(w)
    return answ

def posfunc(xarg):
    count = 0
    nlist = []
    for i in xarg:
        try:
            count = bdata.index(i)
        except ValueError:
            print("not match")
        nlist.append(count)
    findfunc(nlist)

def findfunc(xarg):
    count = 0
    count2 = 0
    global answ
    for j in vdata:
        count = 0
        for i in xarg:
            if j[i] == 0:
                count2 += 1
                break
            else:
                count += 1
                if count == len(xarg):
                    print("find")
                    answ = slist[count2]
                    
