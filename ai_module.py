words = ""
def getdata(data):
    if data == "Hi":
        words = "How are you?"
    elif data == "How are you?":
        words = "I am good! thank you."
    elif data == "Hello!":
        words = "How are you?"
    elif data == "I am good! thank you.":
        words = "Ok."
    else:
        pass
    return words

__version__ = "0.1"
