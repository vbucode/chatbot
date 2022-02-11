# module to vector from answere:reply
from words import words

llist = []
rlist = []
with open("chatbotdatabaseclean.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)

def bow():
    word = Words()
    w = word.load()
    humman = llist
    return humman
def vector():
    word = Words()
    w = words.load()
    
def reply():
    computer = rlist
    return rlist
