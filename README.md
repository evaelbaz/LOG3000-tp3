# Calculatrice simple

**Numéro d'équipe :** 1  

## Objectif
Fournir une calculatrice avec une interface visuelle permettant d’insérer des chiffres et des opérandes, puis de calculer le résultat,tel une calculatrice traditionnelle.

## Prérequis
- Python installé sur la machine  
- `pip` installé et accessible depuis le terminal

## Installation

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/evaelbaz/LOG3000-tp3.git
    cd LOG3000-tp3
    ```

2. Partir un environnement virtuel python 3.12+ (venv) :
    ```bash
    python3.12 -m venv venv
    ```

    Windows:
    ```bash
    venv\Scripts\activate
    ```

    macOs / Linux
    ```bash
    source venv/bin/activate
    ```

3. Installer flask :
    ```bash
    pip install flask
    ```

## Utilisation

Afin d'utiliser l'application, il ne suffit que d'avoir un terminal ouvert à la racine et d'effectuer la commande suivante :
    ```bash
    python app.py
    ```

Une fois l'application ouverte, son utilisation est comme celle d'une calculatrice standard. Il suffit de rentrer un nombre quelconque composé de un ou plusieurs chiffres, suivi d'une opération, et d'un autre nombre. Suite à avoir fait tous les calculs nécessaires, il faut appuyer sur le bouton = afin d'obtenir le résultat.

## Tests

Afin d'effectuer tous les tests proposés, il faut encore une fois avoir un terminal ouvert à la racine du projet et de rouler la commande suivante :

    python tests/test_calculator.py

## Flux de contribution

Lorsqu'un bug est rencontré ou qu'une nouvelle fonctionnalité sera ajoutée, il faut suivres les étapes suivantes :

1. Créer une issue github détaillant le problème à résoudre et ses exigences associées.

2. Créer une branche github pour l'issue en question.

3. Résoudre le problème dans le code de la branch.

4. Faire une pull request.

5. Attendre une revue par un autre membre de l'équipe.

6. Merge la branch dans main.