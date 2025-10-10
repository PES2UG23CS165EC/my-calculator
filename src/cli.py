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
def calculate(operation: str, num1: float, num2: float = None) -> None:
    """
    CLI entry point for calculator.

    Args:
        operation (str): Operation name (add, subtract, multiply, divide, power, sqrt)
        num1 (float): First number
        num2 (float, optional): Second number for binary operations
    """
    try:
        # Mapping two-argument operations
        two_arg_ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power,
        }

        if operation in two_arg_ops:
            if num2 is None:
                raise ValueError(f"{operation.capitalize()} operation requires two numbers")
            func = two_arg_ops[operation]
            result = func(num1, num2)

        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)

        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format output: integer if whole number, else 2 decimal places
        if isinstance(result, float) and result.is_integer():
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}" if isinstance(result, float) else result)

    except (ValueError, TypeError) as exc:  # Only catch known exceptions
        click.echo(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()  # pylint: disable=no-value-for-parameter
