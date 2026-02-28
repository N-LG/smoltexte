 
j'utilise un format de fichier spécifique pour gérer la documentation et je souhaitai adopter un standard pour gérer la documentation, mes critères pour trouver Le bon:
    * éditable par un éditeur de texte
    * permet de créer des chapitres avec un liens interne
    * liens insérable dans un paragraphe
    * legère mise en forme du texte
    * codage acceptant tout les caractère unicode
    * permet d'y inclure des images,son,video
 
 
 
 
le smoltexte est organisé en ligne, les marqueur de fin de ligne peut être CR, LF, ou CRLF
la première ligne est dédié aux métadonnée du fichier, ensuite chaque fonctions d'une ligne est définis par ses premiers caractères. certaines p 
 
 
 
la première ligne est destiné à avertir du format et à contenir les métadonnée du document, celle ci as le format suivant:
 
>SMLTX;titre;auteur;date dernière modification;version;organisation;date de valididité; 
seule la chaine SMLTX; au début est obligatoire pour indiquer de quel type est le document. Les dates sont au format YYYY-MM-JJ ou YYYY-MM-JJThh:mm:ss.ms suivant le jour et l'heure UTC 
 
titre a sous titre (façon gemtext)
tableau (façon markdown)
fichier multimédia    !texte alternatif|url du fichier (un navigateur qui ne supporte pas le type du fichier affichera un lien pour le télécharger)
rubrique
 
 
indentation de la ligne
on ignore le caractère de début de ligne (si on veux faire commencer une ligne par un caractère réservé)
paragraphe spécial(résumé, citations, extrais de code...) ,des indentations avec le symbole ? peuvent être ajouté a la suite  pour la mise en forme et on doit utiliser une police a chasse fixe 
 
 
 
chaque caractère spécial encadre la zone concerné, si on as besoin d'afficher le caractère, on as simplement besoin de le répéter, un seul caractère sera affiché et aucune mise en forme spécifique sera appliqué
 
exemple:
>~nom d'affichage|url~ 
 
 
 
 
 
*
si il n'y as pas d'url, le nom d'affichage correspond a une sous rubrique du même document
si l'url commence par # c'est une sous rubrique du même document
 
 
 
 
 
</body></html>