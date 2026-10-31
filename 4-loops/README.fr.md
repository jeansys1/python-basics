# Python Quiz

[English version](README.md)

Un quiz en ligne de commande avec 10 questions sur les bases de Python. Le programme pose chaque question, vérifie la réponse, compte le score et permet de rejouer.

Projet 4 de ma série **Python Basics** (les bases de Python), sur le thème des **boucles**.

> Le code et les messages du programme sont en anglais, comme c'est l'usage en entreprise.

## Fonctionnalités

- 10 questions à choix multiples sur les variables, les fonctions, les conditions et les boucles
- Si la réponse n'est pas 1, 2 ou 3, le programme redemande
- Affiche la bonne réponse après une erreur
- Score final avec un pourcentage, une barre de score et un message
- On peut rejouer autant de fois qu'on veut

## Exemple

```text
============ PYTHON QUIZ ============
10 questions about Python basics.

Question 1/10: What does input() always return?
  1. A number
  2. A string
  3. A boolean
Your answer (1, 2 or 3): 2
Correct!

Question 2/10: Which keyword creates a function?
  1. def
  2. function
  3. func
Your answer (1, 2 or 3): abc
Please type 1, 2 or 3.
Your answer (1, 2 or 3): 2
Wrong! Right answer: 1. def

...

====================================
Your score: 8/10 (80%)
Score bar: ########--
Great job!
====================================
Play again? (yes/no): no
Thanks for playing!
```

## Lancer le programme

Il faut seulement Python 3, rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/4-loops
python3 python_quiz.py
```

## Ce que j'ai appris

- Répéter du code avec une boucle `for` : un tour pour chaque question
- Utiliser `range()` et `len()` pour numéroter les choix
- Répéter du code avec une boucle `while` tant que la saisie n'est pas valide
- Arrêter une boucle infinie `while True` avec `break` quand le joueur ne veut plus rejouer
- Ranger des données dans une liste de dictionnaires : chaque question a un texte, des choix et une réponse
- Compter avec `score += 1`
- Afficher sur la même ligne avec `print(..., end="")` pour dessiner la barre de score

## Pistes d'amélioration

- **Exceptions** : gérer les saisies inattendues de façon plus propre
- **Bibliothèques** : poser les questions dans un ordre aléatoire avec `random`
- **Fichiers** : charger les questions depuis un fichier

## Série Python Basics

1. Variables : [Monthly Budget](../1-variables)
2. Fonctions : [Trip Cost](../2-functions)
3. Conditions : [Shipping Cost](../3-conditionals)
4. **Boucles : Python Quiz** (ce projet)
5. Exceptions : [Grade Book](../5-exceptions)
