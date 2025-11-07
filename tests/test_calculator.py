"""
Tests unitaires pour l'application calculatrice.

Ce module contient des tests pour toutes les fonctions de l'application,
incluant les opérateurs mathématiques et la fonction de calcul principal.
"""

import unittest
import sys
import os

# Ajouter le répertoire racine au path pour permettre les imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

from operators import add, subtract, multiply, divide
from app import calculate


class TestOperators(unittest.TestCase):
    """Tests unitaires pour les fonctions d'opérateurs mathématiques."""

    def test_add(self):
        """Test de la fonction d'addition."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(10.5, 2.5), 13.0)
        self.assertEqual(add(-10, -5), -15)
        self.assertEqual(add(10, -5), 5)
        self.assertEqual(add(10000, 20000), 30000)

    def test_subtract(self):
        """Test de la fonction de soustraction."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-15, 10), -25)
        self.assertEqual(subtract(3.5, 1.5), 2.0)
        self.assertEqual(subtract(10000, 20000), -10000)

    def test_multiply(self):
        """Test de la fonction de multiplication."""
        self.assertEqual(multiply(10, -5), -50)
        self.assertEqual(multiply(-15, 10), -150)
        self.assertEqual(multiply(3.5, 1.5), 5.25)
        self.assertEqual(multiply(100, 200), 20000)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, -4), 12)

    def test_divide(self):
        """Test de la fonction de division."""
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335, places=10)
        self.assertEqual(divide(10, -5), -2)
        self.assertEqual(divide(-15, 10), -1.5)
        self.assertEqual(divide(3.5, 1.5), 2.3333333333333335)
        self.assertEqual(divide(10000, 20000), 0.5)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(-3, -4), 0.75)

    def test_divide_by_zero(self):
        """Test de la division par zéro."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


class TestCalculate(unittest.TestCase):
    """Tests unitaires pour la fonction calculate() - parsing et validation."""
    
    def test_parsing_basic_expressions(self):
        """Test que calculate() parse correctement les expressions de base."""
        try:
            calculate("5+3")
            calculate("10-2")
            calculate("4*5")
            calculate("20/4")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly: {e}")

    def test_parsing_removes_spaces(self):
        """Test que les espaces sont correctement supprimés lors du parsing."""
        result1 = calculate("5+3")
        result2 = calculate("5 + 3")
        result3 = calculate("  5  +  3  ")
        self.assertEqual(result1, result2)
        self.assertEqual(result1, result3)

    def test_parsing_decimal_numbers(self):
        """Test que les nombres décimaux sont correctement parsés."""
        try:
            calculate("2.5+3.5")
            calculate("10.5-2.5")
            calculate("3.14*2")
            calculate("15.75/3")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly: {e}")

    def test_parsing_large_numbers(self):
        """Test que les grands nombres sont correctement parsés."""
        try:
            calculate("1000+2000")
            calculate("50000-10000")
            calculate("100*1000")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly: {e}")

    def test_parsing_small_numbers(self):
        """Test que les petits nombres décimaux sont correctement parsés."""
        try:
            calculate("0.1+0.2")
            calculate("0.001*100")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly: {e}")

    def test_parsing_all_operators(self):
        """Test que tous les opérateurs supportés sont correctement détectés."""
        try:
            calculate("5+3")
            calculate("5-3")
            calculate("5*3")
            calculate("15/3")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly: {e}")

    def test_empty_expression(self):
        """Test avec une expression vide."""
        with self.assertRaises(ValueError) as context:
            calculate("")
        self.assertIn("empty expression", str(context.exception))

    def test_none_expression(self):
        """Test avec None comme expression."""
        with self.assertRaises(ValueError):
            calculate(None)

    def test_non_string_expression(self):
        """Test avec un type non-string."""
        with self.assertRaises(ValueError):
            calculate(123)

    def test_invalid_expression_no_operator(self):
        """Test avec une expression sans opérateur."""
        with self.assertRaises(ValueError) as context:
            calculate("123")
        self.assertIn("invalid expression format", str(context.exception))

    def test_invalid_expression_multiple_operators(self):
        """Test avec plusieurs opérateurs."""
        with self.assertRaises(ValueError) as context:
            calculate("2+3-1")
        self.assertIn("only one operator is allowed", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            calculate("5*3/2")
        self.assertIn("only one operator is allowed", str(context.exception))

    def test_invalid_expression_non_numeric_left(self):
        """Test avec opérande gauche non numérique."""
        with self.assertRaises(ValueError) as context:
            calculate("abc+5")
        self.assertIn("operands must be numbers", str(context.exception))

    def test_invalid_expression_non_numeric_right(self):
        """Test avec opérande droite non numérique."""
        with self.assertRaises(ValueError) as context:
            calculate("5+def")
        self.assertIn("operands must be numbers", str(context.exception))

    def test_invalid_expression_non_numeric_both(self):
        """Test avec les deux opérandes non numériques."""
        with self.assertRaises(ValueError) as context:
            calculate("abc+def")
        self.assertIn("operands must be numbers", str(context.exception))
        
    def test_negative_numbers(self):
        """Test avec nombres négatifs."""
        try:
            calculate("-5+3")
            calculate("5+-3")
        except Exception as e:
            self.fail(f"calculate() raised {type(e).__name__} unexpectedly with negative numbers: {e}")

    def test_invalid_expression_operator_at_start(self):
        """Test avec opérateur au début (pas d'opérande gauche)."""
        with self.assertRaises(ValueError) as context:
            calculate("+5")
        self.assertIn("invalid expression format", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            calculate("*5")
        self.assertIn("invalid expression format", str(context.exception))

        with self.assertRaises(ValueError) as context:
            calculate("/5")
        self.assertIn("invalid expression format", str(context.exception))

    def test_invalid_expression_operator_at_end(self):
        """Test avec opérateur à la fin (pas d'opérande droite)."""
        with self.assertRaises(ValueError) as context:
            calculate("5+")
        self.assertIn("invalid expression format", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            calculate("10-")
        self.assertIn("invalid expression format", str(context.exception))

        with self.assertRaises(ValueError) as context:
            calculate("10*")
        self.assertIn("invalid expression format", str(context.exception))

        with self.assertRaises(ValueError) as context:
            calculate("10/")
        self.assertIn("invalid expression format", str(context.exception))

    def test_invalid_expression_only_operator(self):
        """Test avec seulement un opérateur."""
        with self.assertRaises(ValueError) as context:
            calculate("+")
        self.assertIn("invalid expression format", str(context.exception))
        with self.assertRaises(ValueError) as context:
            calculate("-")
        self.assertIn("invalid expression format", str(context.exception))
        with self.assertRaises(ValueError) as context:
            calculate("*")
        self.assertIn("invalid expression format", str(context.exception))
        with self.assertRaises(ValueError) as context:
            calculate("/")
        self.assertIn("invalid expression format", str(context.exception))

    def test_invalid_expression_mixed_letters_numbers(self):
        """Test avec mélange de lettres et chiffres."""
        with self.assertRaises(ValueError) as context:
            calculate("5a+3")
        self.assertIn("operands must be numbers", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            calculate("5+3b")
        self.assertIn("operands must be numbers", str(context.exception))


if __name__ == '__main__':
    unittest.main(verbosity=2)
