hauteur= int(input ("hauteur"))

for n in range (0,hauteur):
    if n == 0:
        print (" "*(hauteur-1) +"/" + "\\") #la ligne du haut du triangle
    elif n == (hauteur -1):
        print ("/" + "_" * (n*2) + "\\") # la ligne du bas de triangle
    else:
        print (" "*(hauteur-n-1)+"/"  +" " *(n*2) + "\\") #les lignes du milieu de triangle
