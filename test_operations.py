"""
This module contains tests for arithmetic operations within a calculator application.
"""

from decimal import Decimal  # Standard library imports should come first
import pytest  # Third-party imports come after standard library imports

from calculator.calculation import Calculation
from calculator.operations import divide  # Only import what you use


def test_operation(first_operand, second_operand, operation, expected):
    """
    Testing various operations.
    """
    calculation = Calculation.create(first_operand, second_operand, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"


def test_divide_by_zero():
    """
    Testing the divide by zero exception.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
