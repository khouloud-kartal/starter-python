debut= int(input ("premier chiffre"))
fin= int(input ("dernier chiffre"))

if debut==fin:
    print ("valeurs égales")
elif debut<fin:
    for n in range (debut+1 , fin):
        print (n)
elif debut>fin:
    for n in range (debut-1, fin, -1):
        print (n)