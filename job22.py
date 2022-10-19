import re


chaine_caractere= input ('saisissez une chaine de caractere: ')
fonction= input ('saisissez une fonction: upper, lower, title, clean: ')


def myUpper (chaine_caractere):
    resultat = ' '
    for i in chaine_caractere:
        if ord(i) >= 97 and ord(i) <= 122 :
            resultat += chr(ord(i) - 32)
        else:
            resultat +=i
    return (resultat)


def myLower (chaine_caractere):
    resultat = ' '
    for i in chaine_caractere:
        if ord(i) >= 65 and ord(i) <= 90 :
            resultat += chr(ord(i) + 32)
        else:
            resultat +=i
    return (resultat)


def myTitle (chaine_caractere):

    resultat = re.sub(r'(((?<=\s)|^|-)[a-z])', lambda x: myUpper(x.group()), chaine_caractere)
    
    return (resultat)
         


def myClean (chaine_caractere):
    resultat = re.sub(' +', ' ', chaine_caractere)

    return (resultat)

if fonction == "upper":
    print(myUpper(chaine_caractere))
elif fonction == "lower":
    print(myLower(chaine_caractere))
elif fonction == "title":
    print(myTitle(chaine_caractere))
elif fonction == "clean":
    print(myClean(chaine_caractere))
else:
    print ("L'option n'est reconnu")
    
