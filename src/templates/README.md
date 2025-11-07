# Module templates/

Le module `templates/` contient le templates HTML utilisé pour générer la page web de l'application.

## Fichiers principaux et leurs responsabilités

### `index.html`
- **Responsabilité principale** : Template principal de l'interface utilisateur de la calculatrice
- **Fonctionnalités** :
  - Définit la structure HTML de la page de la calculatrice
  - Contient le formulaire qui envoie les expressions mathématiques au serveur via POST
  - Affiche le résultat des calculs dans un champ de texte en lecture seule
  - Contient les boutons numériques (0-9) et opérateurs (+, -, *, /)
  - Inclut le JavaScript côté client pour :
    - Ajouter des caractères à l'affichage (`appendToDisplay()`)
    - Effacer l'affichage (`clearDisplay()`)

### Dépendances
- **Flask** : Le framework Flask utilise Jinja2 pour rendre les templates
- **Jinja2** : Moteur de template intégré à Flask (installé automatiquement avec Flask)
- **static/style.css** : Le template référence le fichier CSS pour le style

### Hypothèses
- Les variables passées depuis `app.py` sont disponibles dans le contexte du template

### Structure
- Ce répertoire suit la convention Flask standard pour les templates

