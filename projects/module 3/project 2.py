def shutdown(option):
    if option == "yes":
        print("shutting down")
    elif option == "no":
        print("abort shut down")
    else:
        print("sorry")

choice = input("Do you want to shut down? \n")
shutdown(choice)