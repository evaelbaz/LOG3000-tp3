def add(a,b):
    """
    Cette fonction prend deux valeurs, `a` et `b`, en paramètres et retourne leur somme.

    Args:
        a (Any): La première valeur à additionner.
        b (Any): La deuxième valeur à additionner.

    Returns:
        Any: Le résultat de l'addition de `a` et `b`. Le type du résultat dépend des types des opérandes.
    """
    return a + b

def subtract(a,b):
    """
    Cette fonction prend deux valeurs, `a` et `b`, et retourne le résultat de la soustraction de `a` par `b`.

    Args:
        a (Any): La valeur à soustraire.
        b (Any): La valeur dont on soustrait `a`.

    Returns:
        Any: Le résultat de la soustraction de `a` par `b` (c'est-à-dire `b - a`). 
    """

    return b - a

def multiply(a,b):
    """
    Cette fonction prend deux valeurs, `a` et `b`, en paramètres et retourne leur produit.

    Args:
        a (Any): Le premier facteur.
        b (Any): Le second facteur.

    Returns:
        Any: Le produit de `a` et `b`. Le type du résultat dépend des types des opérandes.
    """
    return a * b

def divide(a,b):
    """
    Cette fonction prend deux valeurs, `a` et `b`, en paramètres et retourne le résultat de la division de `a` par `b`.

    Args:
        a (Any): La valeur à diviser.
        b (Any): La valeur par laquelle diviser.

    Returns:
        Any: Le résultat de la division de `a` par `b`. Le type du résultat dépend des types des opérandes.

    Raises:
        ZeroDivisionError: Si `b` est égal à zéro, une exception de type `ZeroDivisionError` est levée.
    """
    return a // b
