# Chatbot
# author Bulat

import app

reply = "try again with more information.."

print("Welcome to: Chatbot")

def main():
    global user
    user = input("\nYou: ")
    ai(user)
def ai(data):
    if not data:
        main()
    elif data == "exit":
        exit()
    send = app.getdata(data)
    if send != "":
        print("\nChatbot: {}".format(send))
    else:
        print("\nChatbot: {}".format(reply))
while  True:
    main()
