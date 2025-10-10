"""
Command Line Interface for Calculator
Example usage:
    python src/cli.py add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple CLI calculator."""

    try:
        # Map operations to functions
        operations_with_two_args = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power,
        }

        if operation in operations_with_two_args:
            if num2 is None:
                raise ValueError(f"{operation.capitalize()} operation requires two numbers")
            func = operations_with_two_args[operation]
            result = func(num1, num2)

        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)

        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Output formatting: integer if whole number, otherwise 2 decimal places
        if isinstance(result, float) and result.is_integer():
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}" if isinstance(result, float) else result)

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
