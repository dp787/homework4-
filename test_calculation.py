"""
Test suite for verifying the functionality of the Calculation class and its operations.
This includes testing basic arithmetic operations and the special case of division by zero.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "first_operand, second_operand, operation, expected_result",
    [
        (Decimal('5'), Decimal('3'), add, Decimal('8')),
        (Decimal('10'), Decimal('2'), subtract, Decimal('8')),
        (Decimal('4'), Decimal('5'), multiply, Decimal('20')),
        (Decimal('20'), Decimal('4'), divide, Decimal('5')),
        # Add more test cases if necessary
    ]
)
def test_calculation_operations(first_operand, second_operand, operation, expected_result):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(first_operand, second_operand, operation)
    assert calc.perform() == expected_result, f"Failed {operation.__name__} operation with {first_operand} and {second_operand}"

def test_calculation_repr():
    """
    Test the string representation of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The repr output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
