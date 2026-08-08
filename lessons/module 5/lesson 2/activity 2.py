class WhatsApp():
    def __init__(self):
        print("creating the object in the constructor")

    def __del__ (self):
        print("destroying the object in the destructor")

print("will now create the object")

chat = WhatsApp()

del chat

print("program ends here...")