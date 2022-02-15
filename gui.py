# Iluza chatbot
# author Bulat

import app

reply = "try again with more information.."

print("Welcome to: Iluza")

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
        print("\nIluza: {}".format(send))
    else:
        print("\nIluza: {}".format(reply))
while  True:
    main()
