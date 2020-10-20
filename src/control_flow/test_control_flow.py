"""
Control flow

@see https://docs.python.org/3/reference/compound_stmts.html

"""

def test_if_statement():
    """IF statement

    @see: https://docs.python.org/3/tutorial/controlflow.html

    There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
    short for ‘else if’, and is useful to avoid excessive indentation.

    An if … elif … elif … sequence is a substitute for the switch or case statements found
    in other languages.
    """

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'

def test_while_statement():
    """WHILE statement

    @see: https://docs.python.org/3/tutorial/controlflow.html
    @see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

    The while loop executes as long as the condition remains true. In Python, like in C, any
    non-zero integer value is true; zero is false. The condition may also be a string or list
    value, in fact any sequence; anything with a non-zero length is true, empty sequences are
    false.

    The test used in the example is a simple comparison. The standard comparison operators are
    written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or
    equal to), >= (greater than or equal to) and != (not equal to).
    """

    # Let's raise the number to certain power using while loop.
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32

# pylint: disable=too-many-locals
def test_for_statement():
    """FOR statement

    @see: https://docs.python.org/3/tutorial/controlflow.html

    The for statement in Python differs a bit from what you may be used to in C or Pascal.
    Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
    giving the user the ability to define both the iteration step and halting condition (as C),
    Python’s for statement iterates over the items of any sequence (a list or a string), in the
    order that they appear in the sequence. For example (no pun intended):
    """


    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" length is 3
    # "window" length is 6
    # "defenestrate" length is 12
    assert words_length == (3 + 6 + 12)

    # If you need to modify the sequence you are iterating over while inside the loop
    # (for example to duplicate selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicitly make a copy. The slice notation makes this
    # especially convenient:
    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    # handy. It generates arithmetic progressions:
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # To iterate over the indices of a sequence, you can combine range() and len() as follows:
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # Or simply use enumerate().
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # When looping through dictionaries, the key and corresponding value can be retrieved at the
    # same time using the items() method.
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # When looping through a sequence, the position index and corresponding value can be retrieved
    # at the same time using the enumerate() function
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # To loop over two or more sequences at the same time, the entries can be paired with
    # the zip() function.
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []

    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]

def test_break_statement():
    """BREAK statement"""

    # Let's terminate the loop in case if we've found the number we need in a range from 0 to 100.
    number_to_be_found = 42
    # This variable will record how many time we've entered the "for" loop.
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            # Break here and don't continue the loop.
            break
        else:
            number_of_iterations += 1

    # We need to make sure that break statement has terminated the loop once it found the number.
    assert number_of_iterations == 42

def test_continue_statement():
    """CONTINUE statement

    @see: https://docs.python.org/3/tutorial/controlflow.html

    The continue statement is borrowed from C, continues with the next iteration of the loop.
    """

    # This list will contain only even numbers from the range.
    even_numbers = []
    # This list will contain every other numbers (in this case - ods).
    rest_of_the_numbers = []

    for number in range(0, 10):
        # Check if remainder after division is zero (which would mean that number is even).
        if number % 2 == 0:
            even_numbers.append(number)
            # Stop current loop iteration and go to the next one immediately.
            continue

        rest_of_the_numbers.append(number)

    assert even_numbers == [0, 2, 4, 6, 8]
    assert rest_of_the_numbers == [1, 3, 5, 7, 9]

def test_range_function():
    """Range function

    If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    handy. It generates arithmetic progressions.

    In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
    It is an object which returns the successive items of the desired sequence when you iterate
    over it, but it doesn’t really make the list, thus saving space.

    We say such an object is iterable, that is, suitable as a target for functions and constructs
    that expect something from which they can obtain successive items until the supply is exhausted.
    We have seen that the for statement is such an iterator. The function list() is another; it
    creates lists from iterables:
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # The given end point is never part of the generated sequence; range(10) generates 10 values,
    # the legal indices for items of a sequence of length 10. It is possible to let the range start
    # at another number, or to specify a different increment (even negative; sometimes this is
    # called the ‘step’):

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
