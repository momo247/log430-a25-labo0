"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests

def test_addition():
    my_calculator = Calculator()
    assert  my_calculator.addition(1, 2) == 3
    assert  my_calculator.addition(40, -10) == 30
    assert  my_calculator.addition(1000000, -1000000) == 0

def test_substraction():
    my_calculator = Calculator()
    assert  my_calculator.subtraction(5, 2) == 3
    assert  my_calculator.subtraction(5, -2) == 7

def test_multiplication():
    my_calculator = Calculator()
    assert  my_calculator.multiplication(5, 5) == 25
    assert  my_calculator.multiplication(10, -2) == -20

def test_division():
    my_calculator = Calculator()
    assert  my_calculator.division(10, 2) == 5
    assert  my_calculator.division(10, -2) == -5
    assert  my_calculator.division(10, 0) == "Erreur : division par zéro"