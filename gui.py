#!/usr/bin/python3
from app import App
import logging

reply = "Я вас не понимаю, пожалуйста, повторите"
#reply = "more information.."

print("Welcome to: ChatBot")

def main():
    user = input("\nYou: ")
    send = App(user)
    logging.info(user)
    if not user:
        print("\nChatbot: {}".format(reply))
    elif user == "exit":
        exit()
    elif len(user) > 10:
        print("\nChatbot: {}".format(reply))
        logging.info(reply) 
    else:
        s = send.getdata()
        if s == "":
            print("\nChatbot: {}".format(reply))
        else:
            print("\nChatbot: {}".format(s))
            logging.info(s)

logging.basicConfig(level=logging.DEBUG,
                    filename = "mylog.log",
                    filemode="a",
                    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S')

while  True:
    main()
