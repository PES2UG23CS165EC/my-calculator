"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b with input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# TODO: Students will add power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

def test_add_negative_numbers(self):
    """Test adding negative numbers"""
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_subtract_negative_numbers(self):
    """Test subtracting negative numbers"""
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2
