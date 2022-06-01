import tkinter
from tkinter import scrolledtext
import logging
from words import Words
from wordvector import WordVector

root = tkinter.Tk()
root.title("chatbot")
root.geometry("405x230")
root.configure(bg = "black")

llist = []
rlist = []
dlist = []
instb = []

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

for i in dlist:
    for j in i:
        instb.append(j)

def send():
    answ = ""
    searchlist = []
    reply = "more information.."
    logging.info(ent.get())
    if not ent.get():
        pass
    else:
        word = Words(ent.get())
        w = word.load()
        ent.delete(0, "end")
        for k in w:
            for i, x in enumerate(instb):
                if x == k:
                    searchlist.append(i)
        if len(w) != 0:
            for i in range(len(dlist)):
                countw = 0
                for k in searchlist:
                    try:
                        if vect[i][k] == 1:
                            countw += 1
                            if countw == len(dlist[i]):
                                answ = rlist[i]
                    except ValueError:
                        pass

    if answ == "":
        r = "Chatbot: " + reply + "\n"
        txt.insert(tkinter.END, r)
        logging.info(r)
    else:
        r = "Chatbot: " + answ + "\n"
        txt.insert(tkinter.END, r)
        logging.info(r)

ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "send", bg = "gray", command = send)
txt = scrolledtext.ScrolledText(root, width = 45, height = 10)
txt.grid(column = 0, row = 0)
ent.place(x = 5, y = 190 )
btn1.place(x = 340, y = 185)

logging.basicConfig( level=logging.DEBUG, filename = "mylog.log", filemode="a", format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", datefmt='%H:%M:%S')

if __name__ == "__main__":
    root.mainloop()
