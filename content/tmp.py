def add(num1, num2):
    return num1 + num2


import pytest


@pytest.mark.parametrize(
    ('input_arg', 'expected'),
    (
        ((1, 2), 3),
        ((2, 3), 5),
    ),
)
def test_add(input_arg, expected):
    assert add(*input_arg) == expected
