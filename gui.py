#!/usr/bin/python3
from app import App

reply = "Я вас не понимаю, пожалуйста, повторите"
#reply = "more information.."

print("Welcome to: ChatBot")

def main():
    user = input("\nYou: ")
    if not user:
        print("\nChatbot: {}".format(reply))
    elif user == "exit":
        exit()
    elif len(user) > 10:
        print("\nChatbot: {}".format(reply))
    else:
        answ(user)
def answ(xarg):
    send = App(xarg)
    s = send.getdata()
    if s == "":
        print("\nChatbot: {}".format(reply))
    else:
        print("\nChatbot: {}".format(s))
while  True:
    main()
