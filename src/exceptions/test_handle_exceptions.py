"""Errors and Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt
is made to execute it. Errors detected during execution are called exceptions and are not
unconditionally fatal.

It is possible to write programs that handle selected exceptions.
"""

def test_handle_exceptions():
    """Handling of exceptions

    The try statement works as follows.

    - First, the try clause (the statement(s) between the try and except keywords) is executed.

    - If no exception occurs, the except clause is skipped and execution of the try statement
    is finished.

    - If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.

    - If an exception occurs which does not match the exception named in the except clause, it is
    passed on to outer try statements; if no handler is found, it is an unhandled exception and
    execution stops with a message.

    In short:

    The "try" block lets you test a block of code for errors.
    The "except" block lets you handle the error.
    The "else" block lets you execute the code if no errors were raised.
    The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
    """

    # Let's simulate division by zero exception.
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Let's simulate undefined variable access exception.
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # name 'spam' is not defined
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # A try statement may have more than one except clause, to specify handlers for different
    # exceptions. At most one handler will be executed. Handlers only handle exceptions that occur
    # in the corresponding try clause, not in other handlers of the same try statement. An except
    # clause may name multiple exceptions as a parenthesized tuple, for example:

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except (ZeroDivisionError, NameError):
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Exception handlers may be chained.
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # The try … except statement has an optional else clause, which, when present, must follow all
    # except clauses. It is useful for code that must be executed if the try clause does not raise
    # an exception. For example:

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired

    # The finally block, if specified, will be executed regardless if the try block raises an
    # error or not.

    message = ''
    try:
        # pylint: undefined-variable
        print(not_existing_variable)  # noqa: F821
    except NameError:
        message += 'Something went wrong.'
    finally:
        message += 'The "try except" is finished.'

    assert message == 'Something went wrong.The "try except" is finished.'

def test_raise_exception():
    """Raising Exceptions.

    @see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

    The raise statement allows the programmer to force a specified exception to occur.
    """
    exception_is_caught = False

    try:
        # The sole argument to raise indicates the exception to be raised. This must be either an
        # exception instance or an exception class (a class that derives from Exception). If an
        # exception class is passed, it will be implicitly instantiated by calling its constructor
        # with no arguments
        raise NameError('HiThere')
    except NameError:
        exception_is_caught = True

    assert exception_is_caught
