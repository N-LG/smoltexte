#ce programme est destiné a comvertir un fichier smoltexte en github flavored markdown



import os

def formatligne(ligne_argument):
    #retire les espaces au début
    #while ligne_argument[0]==' ':
    #    ligne_argument = ligne_argument[1:]
    
    #liens
    ligne_initiale = ligne_argument.split("~")
    ligne_finale = ""
    for i in range(len(ligne_initiale)):
        if(i%2 != 0):
            if ligne_initiale[i]=="":
                ligne_finale= ligne_finale + "~"
            else:
                if "|" in ligne_initiale[i]:
                    nom = ligne_initiale[i].split("|")[0]
                    adresse = ligne_initiale[i].split("|")[1]
                else:
                    nom = ligne_initiale[i]
                    adresse = "#"+nom
                ligne_finale = ligne_finale+'['+nom+']('+adresse+')'
        else:
            ligne_finale = ligne_finale+(ligne_initiale[i])
    #souligné
    ligne_initiale = ligne_finale.split("_")
    ligne_finale = ""
    for i in range(len(ligne_initiale)):
        if(i%2 != 0):
            if ligne_initiale[i]=="":
                ligne_finale= ligne_finale + "_"
            else:
                ligne_finale = ligne_finale+"<ins>"+ligne_initiale[i]+"</ins>"
        else:
            ligne_finale = ligne_finale+ligne_initiale[i]        
    #emphase
    ligne_initiale = ligne_finale.split("@")
    ligne_finale = ""
    for i in range(len(ligne_initiale)):
        if(i%2 != 0):
            if ligne_initiale[i]=="":
                ligne_finale= ligne_finale + "@"
            else:
                ligne_finale = ligne_finale+"***"+ligne_initiale[i]+"***"
        else:
            ligne_finale = ligne_finale+ligne_initiale[i] 

    return ligne_finale


def indenteligne(ligne):
    #if ligne[0]=='"':
    #    ligne = ligne[1:]

    nb=0
    while ligne[0]=='>':
        nb = nb+1
        ligne = ligne[1:]
        
    while nb!=0:
        ligne = "\u00A0\u00A0\u00A0\u00A0"+ligne
        nb = nb-1
    
    return ligne
    


nom_fichier = input("Entrez le nom du fichier 1:")
fichier_entree = open(nom_fichier+".stx", "r", encoding="utf_8")
fichier_sortie = open(nom_fichier+".md", "w", encoding="utf_8")
lignes = fichier_entree.read().splitlines()

#extrait les métadonnées du document
titre= ""
auteur= ""
date = ""
version=""
org=""
valide=""

metadonne = lignes[0].split(";")

if len(metadonne)>1:
    titre = metadonne[1]
    if len(metadonne)>2:
        auteur = metadonne[2]
        if len(metadonne)>3:
            date = metadonne[3]
            if len(metadonne)>4:
                version = metadonne[4]
                if len(metadonne)>5:
                    org = metadonne[5]
                    if len(metadonne)>6:
                        valide = metadonne[6]
del(lignes[0])


#ajoute un caractère pour eviter que les ligne soient vide
for i in range(len(lignes)):
    if len(lignes[i])==0:
        lignes[i]="  "
        
#parcour les ligne pour les transformer
lastligne=""    
for i in range(len(lignes)):

    #texte standard
    if lignes[i][0]!=":" and lignes[i][0]!="|" and lignes[i][0]!='"' and lignes[i][0]!="?" and lignes[i][0]!="!" and lignes[i][0]!="#":
        fichier_sortie.write(formatligne(indenteligne(lignes[i]))+"\u000D\u000A")

    #ignore le premier caractère
    if lignes[i][0]=='?':
        fichier_sortie.write(formatligne(lignes[i][1:])+"\u000D\u000A")


    #ancre/rubrique
    if lignes[i][0]==":":
        fichier_sortie.write('\u000D\u000A')

    #image
    if lignes[i][0]=="!" :
        alternatif = lignes[i][1:].split("|")[0]
        nom_image = lignes[i].split("|")[1]
        fichier_sortie.write('!['+alternatif+']('+nom_image+')')

    #titre et sous titres
    if lignes[i][0]=="#"and lignes[i][1]!="#":
        fichier_sortie.write('# '+formatligne(lignes[i][1:])+"\u000D\u000A")
    if lignes[i][0]=="#" and lignes[i][1]=="#" and lignes[i][2]!="#" :
        fichier_sortie.write('## '+formatligne(lignes[i][2:])+"\u000D\u000A")
    if lignes[i][0]=="#" and lignes[i][1]=="#" and lignes[i][2]=="#" :
        fichier_sortie.write('### '+formatligne(lignes[i][3:])+"\u000D\u000A")


    #paragraphe
    if lignes[i][0]=='"' :
        fichier_sortie.write(">" + formatligne(indenteligne(lignes[i][1:])))




    #tableau
    if lignes[i][0]=='|':
        fichier_sortie.write(lignes[i])
        


    lastligne=lignes[i][0]


#on cloture le fichier  er on ferme tout
fichier_entree.close()
fichier_sortie.close()
print("terminé!")


















