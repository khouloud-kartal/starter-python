
file = open("data.txt", "r")
data = file.read()
mots = data.split()

print("Le nombre de mots: ", len(mots))