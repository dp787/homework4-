"""
This module configures pytest fixtures for generating dynamic test data for calculator operations.
It utilizes the Faker library to create realistic numerical values and supports dynamic generation
of test cases based on the specified number of records.
"""
from decimal import Decimal
from faker import Faker
import pytest

from calculator.operations import add, subtract, multiply, divide

fake = Faker()

@pytest.fixture
def dynamic_param():
    """A no-op fixture used as a marker for dynamic parameterization."""

def generate_test_data(num_records):
    """
    Generates test data for each arithmetic operation.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal('1')
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_name == 'divide' and b == Decimal('0'):
            b = Decimal('1')

        expected = operation_func(a, b) if not (operation_name == 'divide' and b == Decimal('0')) else "ZeroDivisionError"
        yield a, b, operation_name, expected

def pytest_addoption(parser):
    """
    Adds custom command line options for pytest.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Dynamically generate tests based on command line options."""
    if "dynamic_param" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters= [
            (a, b, op_name, expected)
            for a, b, op_name, expected in parameters
        ]
        metafunc.parametrize("a,b,operation_name,expected", modified_parameters)
