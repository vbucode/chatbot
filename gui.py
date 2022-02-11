# Iluza chatbot
# author Bulat

import app

print("Welcome to: Iluza")

reply = "try again.."

def main():
    global user
    user = input("You: ")
    ai(user)
def ai(data):
    if not data:
        print("Iliza: {}".format(reply))
        main()
    responseai = app.getdata(data)
    print("Iluza: {}".format(responseai))
while  True:
    main()
