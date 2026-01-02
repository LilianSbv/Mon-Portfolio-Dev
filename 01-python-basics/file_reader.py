phrases=["la premiere phrase","Ceci est la deuxieme phrase du texte"]

with open ("mon_fichier.txt","w",encoding="utf-8")as f:
    for phrase in phrases:
        
        f.write(phrase+"\n")

    print (" Le fichier à bien été écrit ")
    print (" LE CONTENU DU FICHIER :")

with open ("mon_fichier.txt","r",encoding="utf-8")as f:
    contenu=f.read()
    print(contenu)
