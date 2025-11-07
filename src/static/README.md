# Module static/

## Raison d'être

Le module `static/` contient la feuille de style css utilisé pour l'application.

## Fichiers principaux et leurs responsabilités

### `style.css`
- **Responsabilité principale** : Définit le style visuel de l'interface de la calculatrice
- **Fonctionnalités** :
  - Définit la mise en page générale (centrage, fond, etc.)
  - Stylise la calculatrice (couleurs, bordures, ombres)
  - Définit l'apparence de l'affichage (écran de la calculatrice)
  - Gère les effets de survol (hover) et d'activation (active) des boutons


### Hypothèses
- Le répertoire `static/` est accessible en lecture par Flask

### Structure
- Ce répertoire suit la convention Flask standard pour les fichiers statiques
- Tous les fichiers dans ce répertoire sont accessibles publiquement via l'URL `/static/<nom_fichier>`

