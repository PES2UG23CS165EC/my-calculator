""" Integration Tests - CLI + Calculator Working Together """

import subprocess
import sys
import pytest
from click.testing import CliRunner

class TestCLIIntegrationSubprocess:
    """Test CLI app integrating with calculator using subprocess"""

    def run_cli(self, *args):
        cmd = [sys.executable, '-m', 'src.cli'] + list(args)
        return subprocess.run(cmd, capture_output=True, text=True, cwd='.')

    def test_cli_add_integration(self):
        result = self.run_cli('add', '5', '3')
        assert result.returncode == 0
        assert result.stdout.strip() == '8'

    def test_cli_multiply_integration(self):
        result = self.run_cli('multiply', '4', '7')
        assert result.returncode == 0
        assert result.stdout.strip() == '28'

    def test_cli_divide_integration(self):
        result = self.run_cli('divide', '15', '3')
        assert result.returncode == 0
        assert result.stdout.strip() == '5'

    def test_cli_sqrt_integration(self):
        result = self.run_cli('sqrt', '16')
        assert result.returncode == 0
        assert result.stdout.strip() == '4'

    def test_cli_error_handling_integration(self):
        result = self.run_cli('divide', '10', '0')
        assert result.returncode == 1
        assert 'Cannot divide by zero' in result.stdout

    def test_cli_invalid_operation_integration(self):
        result = self.run_cli('invalid', '1', '2')
        assert result.returncode == 1
        assert 'Unknown operation' in result.stdout


class TestCLIIntegrationInProcess:
    """Test CLI app integrating with calculator using click.CliRunner"""

    def run_cli(self, *args):
        from src.cli import calculate
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def test_cli_add_integration(self):
        res = self.run_cli('add', '5', '3')
        assert res.exit_code == 0
        assert res.output.strip() == '8'

    def test_cli_multiply_integration(self):
        res = self.run_cli('multiply', '4', '7')
        assert res.exit_code == 0
        assert res.output.strip() == '28'

    def test_cli_divide_integration(self):
        res = self.run_cli('divide', '15', '3')
        assert res.exit_code == 0
        assert res.output.strip() == '5'

    def test_cli_sqrt_integration(self):
        res = self.run_cli('sqrt', '16')
        assert res.exit_code == 0
        assert res.output.strip() == '4'

    def test_cli_error_handling_integration(self):
        res = self.run_cli('divide', '10', '0')
        assert res.exit_code == 1
        assert 'Cannot divide by zero' in res.output

    def test_cli_invalid_operation_integration(self):
        res = self.run_cli('invalid', '1', '2')
        assert res.exit_code == 1
        assert 'Unknown operation' in res.output


class TestCalculatorModuleIntegration:
    """Test calculator module functions working together"""

    def test_chained_operations(self):
        from src.calculator import add, multiply, divide
        step1 = add(5, 3)
        step2 = multiply(step1, 2)
        step3 = divide(step2, 4)
        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        from src.calculator import power, square_root, add
        a_squared = power(3, 2)
        b_squared = power(4, 2)
        sum_squares = add(a_squared, b_squared)
        hypotenuse = square_root(sum_squares)
        assert hypotenuse == 5.0
