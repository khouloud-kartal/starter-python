myinput= input (">")

while myinput != "Au revoir":

    if myinput == "Bonjour":    
        print ("Bonjour à toi")
    elif myinput == "Au revoir":
        quit()
    elif myinput != "Bonjour" or "Au revoir":
        print (myinput)
    myinput= input(">")