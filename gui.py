# Iluza chatbot
# author Bulat

import app

print("Welcome to: Iluza")

reply = "try again.."

def main():
    global user
    user = input("\nYou: ")
    ai(user)
def ai(data):
    if not data:
        print("\nIliza: {}".format(reply))
        main()
    responseai = app.getdata(data)
    print("\nIluza: {}".format(responseai))
while  True:
    main()
