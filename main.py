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

def send():
    answ = ""
    searchlist = []
    instb = []
    reply = "more information.."
    logging.info(ent.get())
    if not ent.get():
        pass
    else:
        word = Words(ent.get())
        w = word.load()
        ent.delete(0, "end")
        if len(w) != 0:
            count = 0
            for i in dlist:
                countw = 0
                for j in i:
                    count += 1
                    for k in w:
                        if k == j and vect[dlist.index(i)][count - 1] == 1:
                            countw += 1
                            if countw == len(w) and countw == len(i):
                                answ = rlist[dlist.index(i)]

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
