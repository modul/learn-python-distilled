"""
Operators overview

@see: https://docs.python.org/3/reference/lexical_analysis.html#operators

@note: for brevity, bitwise operators have been left out.
"""

def test_arithmetic_operators():
    """Arithmetic operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Arithmetic operators are used with numeric values to perform common mathematical operations
    """

    # Addition.
    assert 5 + 3 == 8

    # Subtraction.
    assert 5 - 3 == 2

    # Multiplication.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # Division.
    # Result of division is float number.
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Modulus.
    assert 5 % 3 == 2

    # Exponentiation.
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # Floor division.
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)


def test_comparison_operators():
    """Comparison operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Comparison operators are used to compare two values.
    """

    # Equal.
    number = 5
    assert number == 5

    # Not equal.
    number = 5
    assert number != 3

    # Greater than.
    number = 5
    assert number > 3

    # Less than.
    number = 5
    assert number < 8

    # Greater than or equal to
    number = 5
    assert number >= 5
    assert number >= 4

    # Less than or equal to
    number = 5
    assert number <= 5
    assert number <= 6

def test_logical_operators():
    """Logical operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Logical operators are used to combine boolean values.
    """

    # Let's work with these numbers to illustrate logic operators.
    first_number = 5
    second_number = 10

    # and
    # Returns True if both statements are true.
    assert first_number > 0 and second_number < 20

    # or
    # Returns True if one of the statements is true
    assert first_number > 5 or second_number < 20

    # not
    # Reverse the result, returns False if the result is true.
    # pylint: disable=unneeded-not
    assert not first_number == second_number
    assert first_number != second_number

def test_identity_operators():
    """Identity operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Identity operators are used to compare two objects, not for equality, but whether they are actually
    the same object, with the same memory location.
    """

    # Let's illustrate identity operators based on the following lists.
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # Returns true if both variables are the same object.

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    assert first_fruits_list is third_fruits_list

    # is not
    # Returns true if both variables are not the same object.

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    assert first_fruits_list is not second_fruits_list

    # To demonstrate the difference between "is" and "==": this comparison returns True because
    # first_fruits_list is equal to second_fruits_list.
    assert first_fruits_list == second_fruits_list

def test_membership_operators():
    """Membership operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Membership operators are used to test if an element is present in a sequence.
    """

    # Let's use the following fruit list to illustrate membership concept.
    fruit_list = ["apple", "banana"]

    # in
    # Returns True if a sequence with the specified value is present in the object.

    # Returns True because a sequence with the value "banana" is in the list
    assert "banana" in fruit_list

    # not in
    # Returns True if a sequence with the specified value is not present in the object

    # Returns True because a sequence with the value "pineapple" is not in the list.
    assert "pineapple" not in fruit_list

def test_assignment_operator():
    """Assignment operators

    @see: https://www.w3schools.com/python/python_operators.asp

    Assignment operators are used to assign values to variables
    """

    # Assignment: =
    number = 5
    assert number == 5

    # Multiple assignment.
    # The variables first_variable and second_variable simultaneously get the new values 0 and 1.
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # You may even switch variable values using multiple assignment.
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0

def test_augmented_assignment_operators():
    """Assignment operator combined with arithmetic and bitwise operators"""

    # Assignment: +=
    number = 5
    number += 3
    assert number == 8

    # Assignment: -=
    number = 5
    number -= 3
    assert number == 2

    # Assignment: *=
    number = 5
    number *= 3
    assert number == 15

    # Assignment: /=
    number = 8
    number /= 4
    assert number == 2

    # Assignment: %=
    number = 8
    number %= 3
    assert number == 2

    # Assignment: %=
    number = 5
    number %= 3
    assert number == 2

    # Assignment: //=
    number = 5
    number //= 3
    assert number == 1

    # Assignment: **=
    number = 5
    number **= 3
    assert number == 125
