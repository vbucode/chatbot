#!/usr/bin/python3
import app
import logging

reply = "Я вас не понимаю, пожалуйста, повторите"
#reply = "more information.."

print("Welcome to: ChatBot")

def main():
    global user
    user = input("\nYou: ")
    logging.info(user)
    if not user:
        print("\nChatbot: {}".format(reply))
    elif user == "exit":
        exit()
    elif len(user) > 10:
        print("\nChatbot: {}".format(reply))
        logging.info(reply) 
    else:
        send = app.getdata(user)
        if send == "":
            print("\nChatbot: {}".format(reply))
        else:
            print("\nChatbot: {}".format(send))
            logging.info(send)

logging.basicConfig(level=logging.DEBUG,
                    filename = "mylog.log",
                    filemode="a",
                    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S')

while  True:
    main()
