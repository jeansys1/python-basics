# Trip Cost (Coût de Trajet)

[English version](README.md)

Calculateur de trajet en voiture en ligne de commande. On entre la distance, la consommation de la voiture, le prix du carburant, les péages et le nombre de passagers, et le programme affiche le prix du trajet, le prix par personne, la durée et le CO2 émis.

Pratique pour savoir combien chacun doit payer lors d'un covoiturage.

Projet 2 de ma série **Python Basics** (les bases de Python), sur le thème des **fonctions**.

> Le code et les messages du programme sont en anglais, comme c'est l'usage en entreprise.

## Fonctionnalités

- Carburant consommé et prix du carburant
- Prix total à l'aller et en aller-retour, et prix par personne
- Durée du trajet sur route (90 km/h) et sur autoroute (110 km/h)
- CO2 émis au total et par personne
- Les nombres peuvent être écrits avec une virgule (`6,5`) ou un point (`6.5`)

## Exemple

```text
====================================
Trip from Paris to Lyon
====================================
  Distance: 465.0 km
  Fuel used: 30.2 L
  Time on roads (90 km/h): 5 h 10 min
  Time on highway (110 km/h): 4 h 14 min
------------------------------------
COST
  Fuel: 55.92 €
  Tolls: 38.5 €
  One way: 94.42 €
  One way per person: 31.47 €
  Round trip: 188.83 €
  Round trip per person: 62.94 €
------------------------------------
ENVIRONMENT
  CO2 emitted: 69.5 kg
  CO2 per person: 23.2 kg
====================================
```

## Lancer le programme

Il faut seulement Python 3, rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/2-functions
python3 trip_cost.py
```

## Les fonctions du programme

- `main()` : le programme principal, qui demande les informations et affiche le bilan
- `ask_number(question)` : pose une question et renvoie la réponse en nombre
- `calculate_liters(distance, consumption)` : litres de carburant consommés
- `calculate_fuel_cost(liters, fuel_price)` : prix du carburant
- `calculate_co2(liters, kg_per_liter=2.3)` : CO2 émis
- `per_person(total, people)` : divise un total entre les passagers
- `calculate_duration(distance, speed=90)` : durée du trajet en minutes
- `format_duration(minutes)` : transforme `310` en `"5 h 10 min"`

## Ce que j'ai appris

- Créer mes propres fonctions avec `def`
- Donner des paramètres à une fonction et renvoyer un résultat avec `return`
- Donner une valeur par défaut à un paramètre : `calculate_duration(distance)` utilise 90 km/h, `calculate_duration(distance, 110)` utilise 110 km/h
- Réutiliser une même fonction pour plusieurs choses : `per_person()` divise à la fois l'argent et le CO2
- Éviter de répéter du code : `ask_number()` remplace quatre fois la même ligne
- Organiser un programme avec une fonction `main()`
- Convertir des minutes en heures avec `int()`

## Pistes d'amélioration

- **Conditions** : refuser une distance négative ou 0 passager
- **Boucles** : ajouter plusieurs étapes au trajet
- **Exceptions** : redemander un nombre quand la saisie n'en est pas un

## Série Python Basics

1. Variables : [Monthly Budget](../1-variables)
2. **Fonctions : Trip Cost** (ce projet)
3. Conditions : [Shipping Cost](../3-conditionals)
4. Boucles : [Python Quiz](../4-loops)
5. Exceptions : à venir
