## Raison d'être du module templates
Le module static fournit le style à l'interface utilisateur. Sans lui, l'application ne serait que de simples éléments HTML tels des boutons ou du texte de base. Il donne donc une allure de calculatrice au programme en plaçant les boutons et écrans aux bons endroits.

## Fichiers et responsabilités
Ce module donne son style à la calculatrice dans son seul fichier style.css. Il positionne les boutons de la calculatrice en grille. De plus, elle met les boutons en évidence et les regroupe en couleur selon leur fonctionnalité (orange pour les opérations, gris pour les numéros et le clear). Il améliore donc l'expérience utilisateur grandement.

## Dépendances et hypothèses
Pour le foncitonnement de ce module, il faut que le module template définisse bien la structure HTML du programme, importe correctement le fichier style.css et utilise les classes css définies. Il dépend donc de la structure html du programme, soit index.html.