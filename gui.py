# Iluza chatbot
# author Bulat

import app

print("Welcome to: Iluza")

def main():
    global user
    user = input("You: ")
    ai(user)
def ai(data):
    if not data:
        main()
    responseai = ai_module.getdata(data)
    print("Iluza: {}".format(responseai))
while  True:
    main()
