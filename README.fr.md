# Python Basics (les bases de Python)

[English version](README.md)

Cinq petits projets Python, un pour chaque notion de base du langage : **les variables, les fonctions, les conditions, les boucles et les exceptions**.

Je les ai réalisés en suivant le cours **CS50P** de Harvard (*CS50's Introduction to Programming with Python*). Chaque projet utilise seulement ce que le cours avait montré à ce moment-là, pour que le code reste simple et lisible.

> Le code et les messages des programmes sont en anglais, comme c'est l'usage en entreprise.

## Les projets

1. **[Variables : Monthly Budget](1-variables)**
   Un calculateur de budget mensuel : argent restant, budget par jour, projection sur l'année et épargne conseillée.
2. **[Fonctions : Trip Cost](2-functions)**
   Un calculateur de trajet en voiture pour le covoiturage : prix par personne, durée et CO2 émis.
3. **[Conditions : Shipping Cost](3-conditionals)**
   Un calculateur de frais de livraison, comme sur un site e-commerce : prix selon le poids et la destination, livraison offerte et option express.
4. **[Boucles : Python Quiz](4-loops)**
   Un quiz de 10 questions sur les bases de Python, avec une barre de score et la possibilité de rejouer.
5. **[Exceptions : Grade Book](5-exceptions)**
   Un carnet de notes pour une classe : on tape les notes, le programme attrape les mauvaises saisies et redemande, puis affiche la moyenne, la meilleure et la plus basse note et le nombre d'élèves qui ont réussi.

Chaque dossier a son propre README avec un exemple de ce qu'affiche le programme.

## Lancer un projet

Il faut seulement Python 3 (3.10 ou plus récent pour le projet 3), rien à installer.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/1-variables
python3 monthly_budget.py
```

Pour lancer un autre projet, va dans son dossier (`2-functions`, `3-conditionals`, `4-loops`, `5-exceptions`) et lance son fichier `.py`.
