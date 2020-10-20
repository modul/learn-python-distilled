import pytest

def test_tuples():
    """Tuples.

    @see: https://www.w3schools.com/python/python_tuples.asp
    @see: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

    A tuple is a collection which is ordered and unchangeable. In Python tuples are written with
    round brackets.

    The Tuples have following properties:
    - You cannot change values in a tuple.
    - You cannot remove items in a tuple.
    """
    fruits_tuple = ("apple", "banana", "cherry")

    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"

    # You cannot change values in a tuple.
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        fruits_tuple[0] = "pineapple"

    # It is also possible to use the tuple() constructor to make a tuple (note the double
    # round-brackets).
    # The len() function returns the length of the tuple.
    fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))

    assert isinstance(fruits_tuple_via_constructor, tuple)
    assert len(fruits_tuple_via_constructor) == 3

    # It is also possible to omit brackets when initializing tuples.
    another_tuple = 12345, 54321, 'hello!'
    assert another_tuple == (12345, 54321, 'hello!')

    # Tuples may be nested:
    nested_tuple = another_tuple, (1, 2, 3, 4, 5)
    assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # As you see, on output tuples are always enclosed in parentheses, so that nested tuples are
    # interpreted correctly; they may be input with or without surrounding parentheses, although
    # often parentheses are necessary anyway (if the tuple is part of a larger expression). It is
    # not possible to assign to the individual items of a tuple, however it is possible to create
    # tuples which contain mutable objects, such as lists.

    # A special problem is the construction of tuples containing 0 or 1 items: the syntax has some
    # extra quirks to accommodate these. Empty tuples are constructed by an empty pair of
    # parentheses; a tuple with one item is constructed by following a value with a comma (it is
    # not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:
    empty_tuple = ()
    # pylint: disable=len-as-condition
    assert len(empty_tuple) == 0

    # pylint: disable=trailing-comma-tuple
    singleton_tuple = 'hello',  # <-- note trailing comma
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('hello',)

    # The following example is called tuple packing:
    packed_tuple = 12345, 54321, 'hello!'

    # The reverse operation is also possible.
    first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
    assert first_tuple_number == 12345
    assert second_tuple_number == 54321
    assert third_tuple_string == 'hello!'

    # This is called, appropriately enough, sequence unpacking and works for any sequence on the
    # right-hand side. Sequence unpacking requires that there are as many variables on the left
    # side of the equals sign as there are elements in the sequence. Note that multiple assignment
    # is really just a combination of tuple packing and sequence unpacking.

    # Swapping using tuples.
    # Data can be swapped from one variable to another in python using
    # tuples. This eliminates the need to use a 'temp' variable.
    first_number = 123
    second_number = 456
    first_number, second_number = second_number, first_number

    assert first_number == 456
    assert second_number == 123



def test_sets():
    """Sets.

    @see: https://www.w3schools.com/python/python_sets.asp
    @see: https://docs.python.org/3.7/tutorial/datastructures.html#sets

    A set is a collection which is unordered and unindexed.
    In Python sets are written with curly brackets.

    Set objects also support mathematical operations like union, intersection, difference, and
    symmetric difference.
    """
    fruits_set = {"apple", "banana", "cherry"}

    assert isinstance(fruits_set, set)

    # It is also possible to use the set() constructor to make a set.
    # Note the double round-brackets
    fruits_set_via_constructor = set(("apple", "banana", "cherry"))

    assert isinstance(fruits_set_via_constructor, set)

    # You may check if the item is in set by using "in" statement
    assert "apple" in fruits_set
    assert "pineapple" not in fruits_set

    # Use the len() method to return the number of items.
    assert len(fruits_set) == 3

    # You can use the add() object method to add an item.
    fruits_set.add("pineapple")
    assert "pineapple" in fruits_set
    assert len(fruits_set) == 4

    # Use remove() method to remove an item.
    fruits_set.remove("pineapple")
    assert "pineapple" not in fruits_set
    assert len(fruits_set) == 3

    # Demonstrate set operations on unique letters from two word:
    first_char_set = set('abracadabra')
    second_char_set = set('alacazam')

    assert first_char_set == {'a', 'r', 'b', 'c', 'd'}  # unique letters in first word
    assert second_char_set == {'a', 'l', 'c', 'z', 'm'}  # unique letters in second word

    # Letters in first word but not in second.
    assert first_char_set - second_char_set == {'r', 'b', 'd'}

    # Letters in first word or second word or both.
    assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

    # Common letters in both words.
    assert first_char_set & second_char_set == {'a', 'c'}

    # Letters in first or second word but not both.
    assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

    # Similarly to list comprehensions, set comprehensions are also supported:
    word = {char for char in 'abracadabra' if char not in 'abc'}
    assert word == {'r', 'd'}
