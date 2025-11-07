# Module src/

## Raison d'être

Le module `src/` contient toute la logique métier de l'application, incluant le serveur web Flask, les fonctions de calcul mathématique, et la gestion des requêtes HTTP.

## Fichiers principaux et leurs responsabilités

### `app.py`
- **Responsabilité principale** : Point d'entrée de l'application
- **Fonctionnalités** :
  - Initialise l'application
  - Définit la route principale (`/`) qui gère les requêtes GET et POST
  - Contient la fonction `calculate()` qui traite et évalue les expressions mathématiques
  - Gère l'affichage des résultats et des erreurs via le template HTML
- **Dépendances** : Flask, `operators.py`

### `operators.py`
- **Responsabilité principale** : Implémentation des opérations mathématiques de base
- **Fonctionnalités** :
  - Fournit les fonctions `add()`, `subtract()`, `multiply()`, et `divide()`
  - Chaque fonction prend deux opérandes et retourne le résultat de l'opération

### Hypothèses
- Les expressions mathématiques sont limitées à une seule opération binaire (ex: "3+5", "10/2")
- Les opérandes doivent être des nombres valides (entiers ou décimaux)
- Le format d'expression attendu est : `<nombre><opérateur><nombre>` sans espaces
- Les opérateurs supportés sont : `+`, `-`, `*`, `/`

### Structure des répertoires
- `static/` : Contient les fichiers CSS pour le style de l'interface
- `templates/` : Contient les templates HTML pour l'interface utilisateur

