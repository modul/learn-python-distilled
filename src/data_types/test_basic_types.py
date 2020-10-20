import pytest

def test_numbers():
    """Numbers.

    @see: https://docs.python.org/3/tutorial/introduction.html
    @see: https://www.w3schools.com/python/python_numbers.asp

    There are three numeric types in Python:
    - int (e.g. 2, 4, 20)
        - bool (e.g. False and True, acting like 0 and 1)
    - float (e.g. 5.0, 1.6)
    - complex (e.g. 5+6j, 4-3j)
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


    # Booleans
    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"

    # Floating point numbers
    float_number = 7.0
    float_negative = -35.59
    float_number_via_function = float(7)

    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)
    assert float_number == float_number_via_function

    # In exponential notation
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)

def test_string_type():
    """Strings.

    @see: https://docs.python.org/3/tutorial/introduction.html
    @see: https://www.w3schools.com/python/python_strings.asp
    @see: https://www.w3schools.com/python/python_ref_string.asp

    Besides numbers, Python can also manipulate strings, which can be
    expressed in several ways. They can be enclosed in single quotes ('...')
    or double quotes ("...") with the same result.
    """

    # String with double quotes.
    name_1 = "John"
    # String with single quotes.
    name_2 = 'John'
    # Strings created with different kind of quotes are treated the same.
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # \ can be used to escape quotes.
    # use \' to escape the single quote or use double quotes instead.
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # \n means newline.
    multiline_string = 'First line.\nSecond line.'
    # Without print(), \n is included in the output.
    # But with print(), \n produces a new line.
    assert multiline_string == 'First line.\nSecond line.'

    # Strings can be indexed, with the first character having index 0.
    # There is no separate character type; a character is simply a string
    # of size one. Note that since -0 is the same as 0, negative indices
    # start from -1.
    word = 'Python'
    assert word[0] == 'P'  # First character.
    assert word[5] == 'n'  # Fifth character.
    assert word[-1] == 'n'  # Last character.
    assert word[-2] == 'o'  # Second-last character.
    assert word[-6] == 'P'  # Sixth from the end or zeroth from the beginning.

    assert isinstance(word[0], str)

    # In addition to indexing, slicing is also supported. While indexing is
    # used to obtain individual characters, slicing allows you to obtain
    # substring:
    assert word[0:2] == 'Py'  # Characters from position 0 (included) to 2 (excluded).
    assert word[2:5] == 'tho'  # Characters from position 2 (included) to 5 (excluded).

    # Note how the start is always included, and the end always excluded.
    # This makes sure that s[:i] + s[i:] is always equal to s:
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    # Slice indices have useful defaults; an omitted first index defaults to
    # zero, an omitted second index defaults to the size of the string being
    # sliced.
    assert word[:2] == 'Py'  # Character from the beginning to position 2 (excluded).
    assert word[4:] == 'on'  # Characters from position 4 (included) to the end.
    assert word[-2:] == 'on'  # Characters from the second-last (included) to the end.

    # Attempting to use an index that is too large will result in an error.
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # However, out of range slice indexes are handled gracefully when used
    # for slicing:
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python strings cannot be changed — they are immutable. Therefore,
    # assigning to an indexed position in the string
    # results in an error:
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # If you need a different string, you should create a new one:
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # The built-in function len() returns the length of a string:
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # String literals can span multiple lines. One way is using triple-quotes: """..."""
    # or '''...'''. End of lines are automatically included in the string, but it’s possible
    # to prevent this by adding a \ at the end of the line. The following example:
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''

def test_string_operators():
    """Basic operations

    Strings can be concatenated (glued together) with the + operator,
    and repeated with *: 3 times 'un', followed by 'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py' 'thon'
    assert python == 'Python'

    # This feature is particularly useful when you want to break long strings:
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # If you want to concatenate variables or a variable and a literal, use +:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """String methods"""

    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Returns a string where a specified value is replaced with a specified value.
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()

def test_string_formatting():
    """String formatting.

    Often you’ll want more control over the formatting of your output than simply printing
    space-separated values. There are several ways to format output
    """

    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # The str.format() method of strings requires more manual effort. You’ll still use { and } to
    # mark where a variable will be substituted and can provide detailed formatting directives,
    # but you’ll also need to provide the information to be formatted.
    yes_votes = 42_572_654  # equivalent of 42572654
    no_votes = 43_132_495   # equivalent of 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'
