from problems import calculate, parse_input, FormulaError
import pytest

calculate_params = ((1.0, "+", 2.0, 3.0), (1.0, "-", 2.0, -1.0), (3.0, "*", 4.0, 12.0), (80.0, "/", 2.0, 40.0))


@pytest.mark.parametrize("n1,op,n2,expected", calculate_params)
def test_calculate(n1, op, n2, expected):
    assert calculate(n1, op, n2) == expected, f"Calculator failed with inputs {n1=},{op=},{n2=}. Expected {expected}"


def test_calculate_exceptions():
    try:
        calculate(4.0, "add", 8.0)
    except FormulaError:
        assert True
    except Exception:
        assert False, "Failed to raise FormulaError when invalid operation was provided"


parse_params = (("1.0 + 2.0", (1.0, "+", 2.0)), ("1.0 - 2.0", (1.0, "-", 2.0)), ("3.0 * 4.0", (3.0, "*", 4.0)),
                ("80.0 / 2.0", (80.0, "/", 2.0)))


@pytest.mark.parametrize("calculator_input,expected", parse_params)
def test_parse_input(calculator_input: str, expected: tuple[float, str, float]):
    assert parse_input(calculator_input) == expected


def test_parse_exceptions():
    try:
        parse_input("4 + ")
    except FormulaError as e:
        assert str(e) == 'Input does not consist of three elements', "Incorrect exception message when too few elements provided"
    except Exception:
        assert False, "Incorrect exception when too few elements provided"
    else:
        assert False, "No exception raised when too few elements provided"

    try:
        parse_input("eight - forty")
    except FormulaError as e:
        assert str(e) == 'The first and third input value must be numbers', "Incorrect exception message when too few elements provided"
    except Exception:
        assert False, "Incorrect exception when invalid numbers are provided"
    else:
        assert False, "No exception raised when invalid numbers are provided"


full_test_params = (("1.0 + 2.0", 3.0), ("1.0 - 2.0", -1.0), ("3.0 * 4.0", 12.0), ("80.0 / 2.0", 40.0))

@pytest.mark.parametrize("calculator_input,expected", full_test_params)
def test_parse_input(calculator_input: str, expected: float):
    assert calculate(*parse_input(calculator_input)) == expected, "parse_input and calculate did not work together"
