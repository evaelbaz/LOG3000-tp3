## Raison d'être du module templates
Ce module définit la structure de l’interface du programme. Il contient tous les éléments visuels de la calculatrice : les boutons représentant les chiffres, les opérations, le bouton Clear, ainsi que l’écran d’affichage des calculs et des erreurs.

## Fichiers et responsabilités
Ce module contient un seul fichier, soit index.html. Le fichier décrit la structure HTML de la calculatrice. Il affiche les éléments interactifs (boutons, écran) et les messages d’erreur. Il implémente également les fonctions JavaScript responsables de la mise à jour de l’écran et formule les requêtes HTTP destinées au backend dans des balises "script>".

## Dépendances et hypothèses
Pour que le module fonctionne correctement, le backend doit être actif et opérationnel. Sans cela, le fichier HTML n’offre qu’une interface visuelle sans fonctionnalités. Il dépend donc de app.py.