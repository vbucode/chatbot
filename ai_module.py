from words import Words
import json

nlist = []
xlist = []
countiter = 0
flag = 1
with open("simple.txt", "r") as file:
    xlist = file.read().split("\n")

with open("bow.json", "r") as file2:
    bdata = json.load(file2)

with open("vector.json", "r") as file3:
    vdata = json.load(file3)


def getdata(xarg):
    global flag
    global countiter
    word = Words(xarg)
    w = word.load()
    for i in w:
        try:
        #nlist.append(bdata.index[i])
            nlist.append(bdata.index(w))
        except ValueError:
            print("not match")
__version__ = "0.1"
