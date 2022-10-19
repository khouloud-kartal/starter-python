text= input ("écrire un texte")

f= open ("output.txt","a")# le "w" mode: c'est pour écrire mais ça supprime l'encien contenu
f.write (text)
f= open ("output.txt", "r")
print (f.read())
f.close