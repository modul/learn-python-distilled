"""
Function arguments

- default arguments
    @see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
- keyword arguments
    @see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
- arbitrary argument lists
    @see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
- unpacking argument lists
    @see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
"""

import pytest

def test_default_function_arguments():
    """
    Default function arguments

    @see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

    The most useful form is to specify a default value for one or more arguments. This creates a
    function that can be called with fewer arguments than it is defined to allow.
    """

    # The following function raises a number by the given power.
    # By default the function raises number to the power of two.
    def power_of(number, power=2):
        return number ** power

    # This function can be called in several ways because it has default value for
    # the second argument. First we may call it omitting the second argument at all.
    assert power_of(3) == 9
    # We may also want to override the second argument by using the following function calls.
    assert power_of(3, 2) == 9
    assert power_of(3, 3) == 27


def test_function_keyword_arguments():
    """Example of multi-argument function

    @see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

    Functions can be called using keyword arguments of the form kwarg=value.
    """

    # This function accepts one required argument (voltage) and three optional arguments
    # (state, action, and type).
    def parrot(voltage, state='a stiff', action='voom', parrot_type='Norwegian Blue'):
        message = 'This parrot wouldn\'t ' + action + ' '
        message += 'if you put ' + str(voltage) + ' volts through it. '
        message += 'Lovely plumage, the ' + parrot_type + '. '
        message += 'It\'s ' + state + '!'

        return message
    # The parrot function accepts one required argument (voltage) and three optional arguments
    # (state, action, and type). This function can be called in any of the following ways:

    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 1 positional argument
    assert parrot(1000) == message
    # 1 keyword argument
    assert parrot(voltage=1000) == message

    message = (
        "This parrot wouldn't VOOOOOM if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 2 keyword arguments
    assert parrot(voltage=1000000, action='VOOOOOM') == message
    # 2 keyword arguments
    assert parrot(action='VOOOOOM', voltage=1000000) == message

    # 3 positional arguments
    message = (
        "This parrot wouldn't jump if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's bereft of life!"
    )
    assert parrot(1000000, 'bereft of life', 'jump') == message

    # 1 positional, 1 keyword
    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's pushing up the daisies!"
    )
    assert parrot(1000, state='pushing up the daisies') == message

    # But all the following calls would be invalid.

    with pytest.raises(Exception):
        # Required argument missing.
        # pylint: disable=no-value-for-parameter
        parrot()

    # Non-keyword argument after a keyword argument.
    # parrot(voltage=5.0, 'dead')

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        parrot(110, voltage=220)

    with pytest.raises(Exception):
        # unknown keyword argument
        # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
        parrot(actor='John Cleese')

    # In a function call, keyword arguments must follow positional arguments. All the keyword
    # arguments passed must match one of the arguments accepted by the function (e.g. actor is not
    # a valid argument for the parrot function), and their order is not important. This also
    # includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may
    # receive a value more than once. Here’s an example that fails due to this restriction:
    def function_with_one_argument(number):
        return number

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        function_with_one_argument(0, number=0)

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    def test_function(first_param, *arguments, **keywords):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')
        assert keywords == {
            'fourth_param_name': 'fourth named param',
            'fifth_param_name': 'fifth named param'
        }

    test_function(
        'first param',
        'second param',
        'third param',
        fourth_param_name='fourth named param',
        fifth_param_name='fifth named param',
    )

def test_function_arbitrary_arguments():
    """
    Arbitrary Argument Lists

    @see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

    Functions can be called with an arbitrary number of arguments. These arguments will be wrapped up in
    a tuple. Before the variable number of arguments, zero or more normal arguments may occur.
    """

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    def test_function(first_param, *arguments):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')

    test_function('first param', 'second param', 'third param')

    # Normally, these variadic arguments will be last in the list of formal parameters, because
    # they scoop up all remaining input arguments that are passed to the function. Any formal
    # parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that
    # they can only be used as keywords rather than positional arguments.
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'

def test_function_unpacking_arguments():
    """Unpacking Argument Lists

    @see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

    Unpacking arguments may be executed via * and ** operators. See below for further details.
    """

    # The situation may occur when the arguments are already in a list or tuple but need to be
    # unpacked for a function call requiring separate positional arguments. For instance, the
    # built-in range() function expects separate start and stop arguments. If they are not
    # available separately, write the function call with the *-operator to unpack the arguments out
    # of a list or tuple:

    # Normal call with separate arguments:
    assert list(range(3, 6)) == [3, 4, 5]

    # Call with arguments unpacked from a list.
    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'
