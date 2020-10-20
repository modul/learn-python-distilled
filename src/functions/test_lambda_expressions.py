"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.
"""

def test_lambda_expressions():
    """Lambda Expressions"""

    # You can assign an anonymous (lambda) function to a variable and use it like a usual function
    square = lambda x: x * x

    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

    # This function returns the sum of its two arguments: lambda a, b: a+b
    # Like nested function definitions, lambda functions can reference variables from the
    # containing scope.
    def make_increment_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # Another use of lambda is to pass a small function as an argument.
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # Sort pairs by text key.
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
