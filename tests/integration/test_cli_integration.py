"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output"""
        cmd = [sys.executable, "src/cli.py"] + list(args)
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
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Error:") or result.stdout.strip().startswith("Unexpected error:")

    # Multiplication
    def test_cli_multiply_integration(self):
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    # Division
    def test_cli_divide_integration(self):
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        # CLI rounds to 2 decimal places if result is not integer
        assert result.stdout.strip() == "1.67"

    def test_cli_divide_by_zero_error(self):
        result = self.run_cli("divide", "10", "0")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Error:") or result.stdout.strip().startswith("Unexpected error:")

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
        result = self.run_cli("square_root", "-4")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Error:") or result.stdout.strip().startswith("Unexpected error:")
