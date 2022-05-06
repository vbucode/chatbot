import logging
from words import Words
from wordvector import WordVector

llist = []
rlist = []
dlist = []

#reply = "Я вас не понимаю, пожалуйста, повторите"

reply = "more information.."

print("Welcome to: ChatBot")

with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right.replace("\n", ""))

for i in llist:
    vw = Words(i)
    wvl = vw.load()
    dlist.append(wvl)
ivect = WordVector(dlist)
vect = ivect.load()

def main():
    global vect
    global dlist
    answ = ""
    searchlist = []
    instb = []
    user = input("\nYou: ")
    logging.info(user)
    if not user:
        main()
    elif user == "exit":
        exit()
    word = Words(user)
    w = word.load()

    for i in dlist:
        for j in i:
            instb.append(j)
    for k in w:
        for i, x in enumerate(instb):
            if x == k:
                searchlist.append(i)

    if len(searchlist) != 0:
        for j in vect:
            count = 0
            for i in searchlist:
                if j[i] != 0:
                    count += 1
                    if count == len(dlist[vect.index(j)]):
                        answ = rlist[vect.index(j)]
    if answ == "":
        wrong()
    else:
        print("\nChatbot: {}".format(answ))
        logging.info(answ)

def wrong():
    print("\nChatbot: {}".format(reply))
    logging.info(reply)

logging.basicConfig( level=logging.DEBUG, filename = "mylog.log", filemode="a", format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", datefmt='%H:%M:%S')

while  True:
    main()
