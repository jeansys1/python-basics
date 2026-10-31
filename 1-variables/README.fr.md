# Monthly Budget (Budget Mensuel)

[English version](README.md)

Calculateur de budget personnel en ligne de commande. On entre ses revenus et ses dépenses du mois, et le programme affiche un bilan : argent restant, budget par jour, projection sur l'année et épargne conseillée.

Projet 1 de ma série **Python Basics** (les bases de Python), sur le thème des **variables**.

> Le code et les messages du programme sont en anglais, comme c'est l'usage en entreprise.

## Fonctionnalités

- Saisie du salaire, des autres revenus et de 5 dépenses (loyer, courses, transport, abonnements, loisirs)
- Les montants peuvent être écrits avec une virgule (`320,10`) ou un point (`320.10`)
- Part de chaque dépense dans les revenus, en pourcentage
- Argent restant, budget par jour et projection sur 12 mois
- Épargne conseillée selon la règle 50/30/20 (20 % des revenus)

## Exemple

```text
====================================
Jean's budget for November
====================================
INCOME
  Net salary: 2100.0 €
  Other income: 150.0 €
  Total: 2250.0 €
------------------------------------
EXPENSES
  Rent: 750.0 € (33.3% of income)
  Groceries: 320.1 € (14.2% of income)
  Transport: 75.2 € (3.3% of income)
  Subscriptions: 45.0 € (2.0% of income)
  Leisure: 180.0 € (8.0% of income)
  Total: 1370.3 € (60.9% of income)
------------------------------------
SUMMARY
  Money left: 879.7 €
  Per day: 29.32 €
  Over 12 months: 10556.4 €
  Recommended savings (20%): 450.0 €
  Balanced budget: True
====================================
```

## Lancer le programme

Il faut seulement Python 3, rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/1-variables
python3 monthly_budget.py
```

## Ce que j'ai appris

- Créer des variables avec des noms clairs (`money_left`, `budget_per_day`, etc.)
- Les types de base : `str` (le prénom), `float` (les montants), `int` (les constantes `DAYS_PER_MONTH` et `MONTHS_PER_YEAR`) et `bool` (`balanced_budget`)
- Convertir une saisie avec `float()`, car `input()` renvoie toujours du texte
- Faire des calculs avec `+`, `-`, `*`, `/` et arrondir avec `round()`
- Utiliser des constantes, écrites en majuscules
- Utiliser des méthodes de texte : `strip()`, `title()`, `replace()`
- Afficher les résultats avec les f-strings

## Pistes d'amélioration

Ce projet utilise seulement des variables. Les prochains projets de la série m'apprendront de quoi l'améliorer :

- **Fonctions** : éviter de répéter les mêmes lignes pour chaque dépense
- **Conditions** : afficher une alerte quand le budget est dans le rouge
- **Boucles** : pouvoir saisir autant de dépenses que l'on veut
- **Exceptions** : redemander un montant quand la saisie n'est pas un nombre

## Série Python Basics

1. **Variables : Monthly Budget** (ce projet)
2. Fonctions : [Trip Cost](../2-functions)
3. Conditions : [Shipping Cost](../3-conditionals)
4. Boucles : [Python Quiz](../4-loops)
5. Exceptions : [Grade Book](../5-exceptions)
