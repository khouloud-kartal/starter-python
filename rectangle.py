largeur= int(input ("largeur"))
hauteur= int(input ("longeur"))
 
for n in range (0,hauteur):
    if n == 0 or n == (hauteur-1): #la première est dernière ligne
        print ("|" +"-" *largeur +"|")
    else:
        print ("|" + " " * largeur + "|")# les lignes du milieu