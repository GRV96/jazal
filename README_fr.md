# Jazal

Avant qu'une application utilise le chemin d'un fichier, il peut importer de
vérifier s'il a la bonne extension, s'il existe et s'il s'agit d'un dossier ou
d'un fichier. À cette fin, la bibliothèque Jazal fournit la classe PathChecker
et sa sous-classe ReactivePathChecker. Cette dernière permet en plus d'avertir
l'utilisateur que le chemin est invalide et de le remplacer par une valeur
correcte. Ces deux classes ont besoin de pathlib.Path pour fonctionner.

Jazal offre aussi la classe MissingPathArgWarner, qui produit un message
explicite si l'utilisateur omet de fournir un argument chemin obligatoire. Si
le chemin est donné, cette classe peut instancier PathChecker ou
ReactivePathChecker de telle manière que chaque information requise ne soit
donnée qu'une seule fois. Si un chemin optionel est omis, MissingPathArgWarner
peut fournir l'extension appropriée, permettant de générer une valeur par
défaut.

De plus, cette bibliothèque contient des fonctions qui aident à produire des
valeurs par défaut pour des chemins manquants ou invalides.

Voir le script demo.py pour savoir comment employer Jazal.

