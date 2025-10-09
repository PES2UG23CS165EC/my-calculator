"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root


# Operations that require two numbers
TWO_OPERAND_OPS = {"add", "subtract", "multiply", "divide", "power"}

@click.command()
@click.argument("operation")
@click.argument("numbers", type=float, nargs=-1)  # Accept 1 or 2 numbers
def calculate(operation, numbers):
    """Simple calculator CLI"""

    try:
        if len(numbers) == 0:
            click.echo("Error: You must provide at least one number")
            sys.exit(1)

        num1 = numbers[0]
        num2 = numbers[1] if len(numbers) > 1 else None

        # Check if operation requires two numbers
        if operation in TWO_OPERAND_OPS and num2 is None:
            raise ValueError(f"{operation.capitalize()} operation requires two numbers")

        # Perform the requested operation
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Nicely format result: show integer if no decimal part
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except TypeError as e:
        click.echo(f"Type Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
