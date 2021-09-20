"""
Let's build a simple calculator! It takes three arguments: a number, an string denoting an operator, and another number.
It will perform the operation between the two numbers and return the result.

The operators that must be handled are:
"+": Adds the numbers
"-": Subtracts the first number from the second
"*": Multiplies the numbers
"/": Divides the first number by the second. Use float division, so just one slash

This calculator must use a new user defined exception named 'FormulaError', that is thrown when an invalid operator
is given as an argument.
"""


def calculate(n1: float, op: str, n2: float) -> float:
    pass


"""
Now, create a parse_input function for the calculator. This function will take a string as input. Attempt to parse
the string into a number, followed by the operator, followed by another number. Return these values as a tuple
in that order.

If three things are not found in the string, raise a FormulaError stating 'Input does not consist of three elements'

When you attempt to convert the numbers into floats, if that cannot be accomplished catch the exception and
raise a FormulaError stating 'The first and third input value must be numbers'
"""


def parse_input(calculator_input: str) -> tuple[float, str, float]:
    pass
