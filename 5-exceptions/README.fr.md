# Grade Book

[English version](README.md)

Un carnet de notes en ligne de commande. On tape le nom et la note de chaque élève, et le programme affiche un rapport : le niveau de chaque élève, la moyenne de la classe, la meilleure et la plus basse note, et le nombre d'élèves qui ont réussi. Si on tape autre chose qu'un nombre, le programme ne plante pas : il redemande.

Projet 5 de ma série **Python Basics** (les bases de Python), sur le thème des **exceptions**.

> Le code et les messages du programme sont en anglais, comme c'est l'usage en entreprise.

## Fonctionnalités

- Ajouter autant d'élèves qu'on veut, et terminer avec un nom vide
- Si la note n'est pas un nombre (comme `abc`), le programme attrape l'erreur et redemande au lieu de planter
- Si la note n'est pas entre 0 et 100, le programme redemande
- La virgule ou le point sont acceptés pour les décimales (`87,5` ou `87.5`)
- Un niveau pour chaque élève : Excellent, Very good, Good, Pass ou Fail
- Moyenne de la classe, meilleure note, note la plus basse et nombre d'élèves qui ont réussi

## Exemple

```text
============ GRADE BOOK ============
Grades go from 0 to 100 (a comma or a dot is fine).
Leave the name empty to finish.

Student name: emma
Emma's grade: abc
That is not a number, please try again.
Emma's grade: 150
The grade must be between 0 and 100.
Emma's grade: 87,5

Student name: leo
Leo's grade: 42

Student name: sara
Sara's grade: 91

Student name:

============== REPORT ==============
  Emma: 87.5 (Very good)
  Leo: 42.0 (Fail)
  Sara: 91.0 (Excellent)
------------------------------------
  Class average: 73.5
  Best grade: Sara (91.0)
  Lowest grade: Leo (42.0)
  Passed: 2 out of 3
====================================
```

## Lancer le programme

Il faut seulement Python 3, rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/5-exceptions
python3 grade_book.py
```

## Ce que j'ai appris

- Attraper une erreur avec `try` et `except` : `float()` lève une `ValueError` quand le texte n'est pas un nombre
- Utiliser `else` après `except` pour exécuter du code seulement quand il n'y a pas eu d'erreur
- Répéter une question avec `while True` jusqu'à ce que la réponse soit valide, dans une fonction qui ne renvoie qu'une bonne valeur
- Vérifier un intervalle avec une comparaison enchaînée : `0 <= grade <= 100`
- Ranger les élèves dans une liste de dictionnaires (un nom et une note) et la parcourir
- Garder le total, la meilleure et la plus basse note dans des variables mises à jour dans la boucle

## Pistes d'amélioration

- **Bibliothèques** : utiliser le module `statistics` pour la moyenne et la médiane
- **Fichiers** : enregistrer les notes dans un fichier et les recharger la fois suivante
- **Tests unitaires** : tester `get_level()` avec quelques notes

## Série Python Basics

1. Variables : [Monthly Budget](../1-variables)
2. Fonctions : [Trip Cost](../2-functions)
3. Conditions : [Shipping Cost](../3-conditionals)
4. Boucles : [Python Quiz](../4-loops)
5. **Exceptions : Grade Book** (ce projet)
