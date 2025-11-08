## Raison d'être du module templates
Le module static fournit le style à l'interface utilisateur. Sans lui, l'application ne serait composée que de simples éléments HTML tels que des boutons ou du texte de base. Il donne donc une allure de calculatrice au programme en plaçant les boutons et les écrans aux bons endroits.

## Fichiers et responsabilités
Ce module donne son style à la calculatrice dans son unique fichier style.css. Il positionne les boutons de la calculatrice en grille. De plus, il met les boutons en évidence et les regroupe par couleur selon leur fonctionnalité (orange pour les opérations, gris pour les numéros et le clear). Il améliore donc grandement l'expérience utilisateur.

## Dépendances et hypothèses
Pour le fonctionnement de ce module, il faut que le module template définisse correctement la structure HTML du programme, importe le fichier style.css et utilise les classes CSS définies. Il dépend donc de la structure HTML du programme, soit index.html.
