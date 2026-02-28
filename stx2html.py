#ce programme est destiné a comvertir un fichier smoltexte en document html



import os

def formatligne(ligne_argument):
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
                ligne_finale = ligne_finale+'<a href="'+adresse+'">'+nom+"</a>"
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
                ligne_finale = ligne_finale+"<u>"+ligne_initiale[i]+"</u>"
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
                ligne_finale = ligne_finale+"<em>"+ligne_initiale[i]+"</em>"
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
fichier_sortie = open(nom_fichier+".html", "w", encoding="utf_8")
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

#écrit les métadonnées
fichier_sortie.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><link href="smoltexte.css" type="text/css" rel="stylesheet" />')
if titre!="":
    fichier_sortie.write('<title>'+titre+'</title>')
fichier_sortie.write('</head><body>')


#ajoute un caractère pour eviter que les ligne soient vide
for i in range(len(lignes)):
    if len(lignes[i])==0:
        lignes[i]=" "
        
#parcour les ligne pour les transformer
lastligne=""    
for i in range(len(lignes)):

    #fin paragraphe
    if lignes[i][0]!='"' and lastligne=='"' :
        fichier_sortie.write('</pre><br/>')

    #fin tableau
    if lignes[i][0]!='|' and lastligne=="|":
        fichier_sortie.write('</table>')

    #texte standard
    if lignes[i][0]!="#" and lignes[i][0]!=":" and lignes[i][0]!="|" and lignes[i][0]!='"' and lignes[i][0]!="?" and lignes[i][0]!="!":
        fichier_sortie.write(formatligne(indenteligne(lignes[i]))+"<br/>")

    #ignore le premier caractère
    if lignes[i][0]=='?':
        fichier_sortie.write(formatligne(lignes[i][1:])+"<br/>")


    #ancre/rubrique
    if lignes[i][0]==":":
        fichier_sortie.write('<hr>')
        motclefs=lignes[i].split(":")
        for j in range(len(motclefs)-1):
            fichier_sortie.write('<a id="'+motclefs[j+1]+'"></a>')

    #titre et sous titres
    if lignes[i][0]=="#"and lignes[i][1]!="#":
        fichier_sortie.write('<h1>'+formatligne(lignes[i][1:])+'</h1><a id="'+formatligne(lignes[i][1:])+'"></a>')
    if lignes[i][0]=="#" and lignes[i][1]=="#" and lignes[i][2]!="#" :
        fichier_sortie.write('<h2>'+formatligne(lignes[i][2:])+'</h2><a id="'+formatligne(lignes[i][2:])+'"></a>')
    if lignes[i][0]=="#" and lignes[i][1]=="#" and lignes[i][2]=="#" :
        fichier_sortie.write('<h3>'+formatligne(lignes[i][3:])+'</h3><a id="'+formatligne(lignes[i][3:])+'"></a>')

    #image
    if lignes[i][0]=="!" :
        alternatif = lignes[i][1:].split("|")[0]
        nom_image = lignes[i].split("|")[1]
        fichier_sortie.write('<img src="'+nom_image+'" alt='+alternatif+'>')


    #début paragraphe
    if lignes[i][0]=='"' and lastligne!='"' :
        fichier_sortie.write('<pre>')

    #paragraphe
    if lignes[i][0]=='"' :
        fichier_sortie.write(formatligne(indenteligne(lignes[i][1:]))+"<br/>")


    #début tableau
    if lignes[i][0]=='|' and lastligne!="|":
        fichier_sortie.write('<table>')

    #tableau
    if lignes[i][0]=='|':
        fichier_sortie.write('<tr>')
        cases = lignes[i][1:].split("|")
        for j in range(len(cases)):
            fichier_sortie.write('<td>'+cases[j]+'</td>')
        fichier_sortie.write('</tr>')


    lastligne=lignes[i][0]


#on cloture le fichier  er on ferme tout
fichier_sortie.write("</body></html>")
fichier_entree.close()
fichier_sortie.close()
print("terminé!")


















