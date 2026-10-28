# Shipping Cost (Frais de Livraison)

[English version](README.md)

Calculateur de frais de livraison en ligne de commande, comme sur un site e-commerce. On entre le poids du colis, le montant du panier, la destination et l'option express, et le programme affiche la facture avec le délai de livraison.

Projet 3 de ma série **Python Basics** (les bases de Python), sur le thème des **conditions**.

> Le code et les messages du programme sont en anglais, comme c'est l'usage en entreprise.

## Les règles de livraison

- **Prix de base selon la destination** : France 4.99 €, Europe 9.99 €, Monde 19.99 €
- **Supplément selon le poids** : jusqu'à 1 kg gratuit, jusqu'à 5 kg +3 €, jusqu'à 10 kg +7 €, au-delà +15 €
- **Livraison offerte** dès 50 € d'achat en France et dès 100 € en Europe
- **Option express** : +5.90 € en France et en Europe, +14.90 € dans le reste du monde
- **Délais** : France 2 à 3 jours (24 h en express), Europe 4 à 6 jours (2 jours en express), Monde 7 à 14 jours (4 jours en express)
- Les colis de plus de 30 kg sont refusés

Si le panier n'atteint pas le montant de la livraison offerte, le programme indique combien il manque.

## Exemple

```text
Package weight (kg): 12
Cart total (€): 80
Destination (France, Europe or World): europe
Express shipping? (yes/no): no

====================================
Shipping invoice
====================================
  Destination: Europe
  Package weight: 12.0 kg
  Shipping: Standard
  Estimated delivery: 4 to 6 days
------------------------------------
  Cart: 80.0 €
  Standard shipping: 24.99 €
------------------------------------
  TOTAL: 104.99 €
====================================
Tip: add 20.0 € to your cart to get free shipping.
```

## Lancer le programme

Il faut Python 3.10 ou plus récent (pour `match`), rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/3-conditionals
python3 shipping_cost.py
```

## Ce que j'ai appris

- Prendre des décisions avec `if`, `elif` et `else`
- Comparer des valeurs avec `<`, `<=`, `>`, `>=` et `==`
- Combiner plusieurs conditions avec `and` et `or`
- Choisir entre plusieurs valeurs avec `match` et `case`, et regrouper des cas avec `|` (`case "france" | "europe"`)
- Écrire des fonctions qui renvoient `True` ou `False`, comme `is_valid_zone()` et `is_free_shipping()`
- Vérifier la saisie avant de calculer : colis trop lourd ou destination inconnue

## Pistes d'amélioration

- **Boucles** : redemander la destination tant qu'elle n'est pas valide, ou commander plusieurs colis
- **Exceptions** : redemander un nombre quand la saisie n'en est pas un

## Série Python Basics

1. Variables : [Monthly Budget](../1-variables)
2. Fonctions : [Trip Cost](../2-functions)
3. **Conditions : Shipping Cost** (ce projet)
4. Boucles : à venir
5. Exceptions : à venir
