from cicd.factorial import factorial
import pytest


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_one():
    assert factorial(1) == 1


@pytest.mark.skip(reason="Missing implementation")
def test_factorial_of_three():
    pass


def test_factorial_of_negative():
    with pytest.raises(ValueError):
        factorial(-1)
