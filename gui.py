# chatbot
# author Bulat

import app
import logging

#reply = "Я вас не понимаю, пожалуйста, повторите"
reply = "more information.."

print("Welcome to: ChatBot")

def main():
    global user
    user = input("\nYou: ")
    logging.info(user)
    ai(user)
def ai(data):
    if not data:
        main()
    elif data == "exit":
        exit()
    elif len(data) > 40:
        wrong()
    send = app.getdata(data)
    if send == "":
        wrong()
    else:
        print("\nChatbot: {}".format(send))
        logging.info(send)

def wrong():
    print("\nChatbot: {}".format(reply))
    logging.info(reply)

logging.basicConfig( level=logging.DEBUG, filename = "mylog.log", filemode="a", format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", datefmt='%H:%M:%S')

while  True:
    main()
