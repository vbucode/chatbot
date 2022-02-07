# IluzaAI chatbot
# in command line 
# author Bulat

import ai_module

print("Welcome to:\nIluza")

def main():
    global user
    user = input("You: ")
    ai(user)
def ai(data):
    responseai = ai_module.getdata(data)
    print("Iluza: {}".format(responseai))
while  True:
    main()
