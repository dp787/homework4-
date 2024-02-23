"""
This test module is designed to validate the functionality of the `calculate_and_print` function within the `main` module. It employs the pytest framework to systematically test a variety of input scenarios, ensuring that the function accurately performs basic arithmetic operations: addition, subtraction, multiplication, and division.

Through the use of parameterized tests, the module covers a wide range of cases, including:
- Basic arithmetic operations with positive and negative integers.
- Error handling for division by zero to prevent runtime errors.
- Validation of input types to ensure that non-numeric inputs are appropriately handled.

The tests aim to ensure that the `calculate_and_print` function not only returns the correct calculation results but also provides meaningful error messages for invalid inputs or operations. This approach helps in maintaining the reliability and robustness of the function across different input conditions.

Dependencies:
- pytest: Used for writing and running the tests.
- main: The module containing the `calculate_and_print` function to be tested.
"""

import pytest
from main import calculate_and_print

@pytest.mark.parametrize(
    "a_string, b_string, operation_string, expected_string",
    [
        ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
        ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
        ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
        ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
        ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
        ("9", "3", 'unknown', "Unknown operation: unknown"),
        ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
        ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
    ]
)
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
    Tests the calculate_and_print function with different sets of inputs and operations.
    Verifies that the output is as expected for both successful operations and error conditions.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
