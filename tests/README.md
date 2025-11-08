## Exécution des tests
Afin d'exécuter les tests, il suffit seulement d'ouvrir un terminal à la racine de l'application et de rouler la commande suivante :

```bash
python tests/test_calculator.py
```

## Couverture
Les tests de ce module couvrent le fonctionnement approprié des opérateurs de la calculatrice ainsi que le calcul de la calculatrice. Les points testés :
- Le fonctionnement approprié des opérateurs.
- Le parsing de chaînes à une opération d'une entrée reçue (espaces en trop, calculs de décimaux, etc.).
- Les expressions invalides (5 +, /, a + 5).
- Les paramètres de types incorrects.
