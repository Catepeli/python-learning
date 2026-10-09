# 🐍 Apprentissage de Python

Bienvenue sur mon dépôt dédié à l'apprentissage du langage de programmation **Python** !
Vous trouverez ici mes notes, mes exercices et (bientôt) mes premiers projets pour progresser pas à pas.

## Jour 1 -> Conversion de température
### Consigne
Écrire un script qui convertit une température de Celsius en Fahrenheit, demandée en entrée par un utilisateur (input).

**Notions travaillées :
fonctions, `input`, f-strings,**

Ce premier exercice touche 4 notions de base (fonction, entrée utilisateur, conversion de type, f-string)
- Pas de complexité annexe,
- Le résultat est vérifiable à la main

## Jour 2 -> Calculateur de moyenne
### Consigne
Ecrire un script qui demande un nombre de notes à l'utilisateur, puis chaque note une par une, et affiche la moyenne à la fin.
### Objectif
Manipuler une liste et une boucle, deux notions qui n'apparaissaient pas encore.

**Notions travaillées :
Listes (list), boucle for avec range, méthode .append(), fonction sum()**

## Jour 3 -> Saisie sécurisée d’un nombre
### Principe illustré
La gestion des erreurs avec try/except.
En Python, quand une opération échoue (convertir “abc” en nombre, diviser par zéro), le programme lève une exception et s’arrête.
'''try/except''' permet d’intercepter cette erreur et de décider quoi faire à la place.
C’est un principe central : on ne fait jamais confiance à une entrée utilisateur.
Il corrige directement les limites relevées aux jours 1 et 2.

### Consigne
Ecrire une fonction demander_nombre(message) qui :
- affiche message et lit la saisie de l’utilisateur ;
- si la saisie est un nombre valide, le renvoie ;
- sinon, affiche « Saisie invalide, recommence. » et redemande, jusqu’à obtenir un nombre correct.

Ensuite, il faut l'utiliser dans un main() qui demande deux nombres et affiche leur division, en affichant un message clair si le second vaut 0 au lieu de planter.

**Notions travaillées :
try/except ValueError : intercepter l’échec de float() sur une saisie non numérique
try/except ZeroDivisionError : intercepter la division par zéro
boucle while True + return : répéter jusqu’à obtenir une saisie valide**

## Jour 4 -> Compteur de mots
### Principe illustré
Le dictionnaire (dict).
Une liste range des valeurs par position (0, 1, 2...).
Un dictionnaire associe une clé à une valeur, comme un vrai dictionnaire associe un mot à sa définition.
C’est l’une des structures les plus utilisées en Python : configuration, données JSON, comptages, index.

### Consigne
Ecrire un script qui :

- demande une phrase à l’utilisateur ;
- compte combien de fois chaque mot apparaît ;
- affiche le résultat, un mot par ligne.

Exemple attendu :
Phrase : le chat et le chien et le lapin
le : 3
chat : 1
et : 2
chien : 1
lapin : 1

**Notions travaillées :

.lower() met la phrase en minuscules, pour que « Le » et « le » soient comptés ensemble
.split() découpe une phrase en liste de mots, en coupant sur les espaces
un dictionnaire vide compteur = {}, rempli au fil d’une boucle for
.items() parcourt un dictionnaire en récupérant à la fois la clé et la valeur**


