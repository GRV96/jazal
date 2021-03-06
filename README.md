# Jazal

## Français

Avant qu'une application utilise le chemin d'un fichier, il peut importer de
vérifier s'il a la bonne extension, s'il existe et s'il s'agit d'un dossier ou
d'un fichier. À cette fin, la bibliothèque Jazal fournit la classe PathChecker
et sa sous-classe ReactivePathChecker. Cette dernière permet en plus d'avertir
l'utilisateur que le chemin est invalide et de le remplacer par une valeur
correcte. Ces deux classes dépendent de pathlib.Path.

Jazal offre aussi la classe MissingPathArgWarner, qui produit un message
explicite si l'utilisateur omet de fournir un argument chemin obligatoire. Si
le chemin est donné, cette classe peut instancier PathChecker ou
ReactivePathChecker de telle manière que chaque information requise ne soit
donnée qu'une seule fois. Si un chemin optionnel est omis, MissingPathArgWarner
peut aider à générer une valeur par défaut en fournissant l'extension attendue.

De plus, cette bibliothèque contient des fonctions qui aident à produire des
valeurs par défaut pour les chemins manquants ou invalides.

Voir les scripts `demo_with_files.py` et `demo_with_dirs.py` pour savoir
comment employer Jazal.

Le nom de cette bibliothèque vient de la chanson polonaise
[*Hej, sokoły!*](https://www.youtube.com/watch?v=ZzZ1qmXZBuY). La répétition du
mot *żal* [ʒal] dans les paroles a insprié le nom Jazal.

### Tests unitaires de Jazal

Les tests unitaires de cette bibliothèque dépendent du cadriciel pytest. Pour
lancer une suite de tests contenue dans le dossier `tests`, écrivez en ligne de
commande une instruction correspondant au modèle suivant.

```
pytest <file name>.py
```

Exécutez le script run_all_tests.py pour lancer tous les tests.

```
python run_all_tests.py
```

Puisque plusieurs tests utilisent des chemins relatifs menant à un dossier et
à un fichier réels, lancez-les depuis le dossier `tests` pour éviter des
exceptions.

## English

Before an application uses a path to a file, it may be important to verify
whether it has the right extension, whether it exists and whether it points to
a directory or a file. For this purpose, library Jazal provides class
PathChecker and its subclass ReactivePathChecker. The latter is also able to
warn the user about invalid paths and make correct ones. These two classes
depend on pathlib.Path.

Jazal also offers class MissingPathArgWarner, which makes an explicit message
if the user omits to provide a mandatory path argument. If the path is given,
this class can instantiate PathChecker or ReactivePathChecker in such a way
that each required information is given only once. If an optional path is
omitted, MissingPathArgWarner can help generating a default value by providing
the expected extension.

In addition, this library contains functions that help making default values
for missing or invalid paths.

See scripts `demo_with_files.py` and `demo_with_dirs.py` to know how to use
Jazal.

This library's name is based on the Polish song
[*Hej, sokoły!*](https://www.youtube.com/watch?v=ZzZ1qmXZBuY). The repetition
of the word *żal* [ʒal] in the lyrics inspired the name Jazal.

### Jazal Unit Tests

This library's unit tests depend on framework pytest. In order to run a test
suite contained in directory `tests`, type an instruction matching the
following template in command line.

```
pytest <file name>.py
```

Execute script run_all_tests.py to perform all the tests.

```
python run_all_tests.py
```

Since several tests use relative paths to an actual directory and an actual
file, run them from directory `tests` to prevent exceptions.
