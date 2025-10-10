"""
Integration Tests - CLI + Calculator Working Together
"""

import sys
import subprocess
from src.calculator import add, subtract, multiply, divide, power, square_root


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """
        Helper method to run the CLI and capture output.
        Uses 'python -m src.CLI' to match your actual file name.
        """
        cmd = [sys.executable, "-m", "src.CLI"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    # Addition
    def test_cli_add_integration(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    # Subtraction
    def test_cli_subtract_integration(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode != 0
        output = result.stdout.strip() or result.stderr.strip()
        assert output.startswith("Error:")

    # Multiplication
    def test_cli_multiply_integration(self):
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    # Division
    def test_cli_divide_integration(self):
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "1.67"  # rounded to 2 decimals

    def test_cli_divide_by_zero_error(self):
        result = self.run_cli("divide", "10", "0")
        assert result.returncode != 0
        output = result.stdout.strip() or result.stderr.strip()
        assert output.startswith("Error:")

    # Power
    def test_cli_power_integration(self):
        result = self.run_cli("power", "2", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    # Square root
    def test_cli_square_root_integration(self):
        result = self.run_cli("square_root", "16")
        assert result.returncode == 0
        assert result.stdout.strip() == "4"

    def test_cli_square_root_negative_error(self):
        # Use '--' to prevent Click from interpreting -4 as an option
        result = self.run_cli("square_root", "--", "-4")
        assert result.returncode != 0
        output = result.stdout.strip() or result.stderr.strip()
        assert output.startswith("Error:")
