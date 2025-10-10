"""
Calculator Module - Basic arithmetic operations.
Provides add, subtract, multiply, divide, power, and square_root functions.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of a and b.
    
    Raises:
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Return the division of a by b.
    
    Raises:
        TypeError: If either a or b is not a number.
        ValueError: If b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Return a raised to the power of b."""
    return a ** b


def square_root(a: Number) -> float:
    """
    Return the square root of a.
    
    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
