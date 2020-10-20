> This is the stripped down version of [Learn
Python](https://github.com/trekhleb/learn-python) by
[Oleksii Trekhleb](https://github.com/trekhleb). If you are missing
something here, go ahead and check out the more comprehensive original
repository.

# Playground and Cheatsheet for Learning Python – Distilled version

> This is a collection of Python scripts that are split by [topics](#table-of-contents) and contain
code examples with explanations, different use cases and links to further readings.

It is a **playground** because you may change or add the code to see how it works
and [test it out](#testing-the-code) using assertions. It also allows you
to [lint the code](#linting-the-code) you've wrote and check if it fits to Python code style guide.
Altogether it might make your learning process to be more interactive and it might help you to keep
code quality pretty high from very beginning.

It is a **cheatsheet** because you may get back to these code examples once you want to recap the
syntax of [standard Python statements and constructions](#table-of-contents). Also because the
code is full of assertions you'll be able to see expected functions/statements output right away
without launching them.

## Documentation

Python homepage: https://python.org

Language reference: https://docs.python.org/3/reference/index.html

Standard library reference: https://docs.python.org/3/library/index.html

## How to Use This Repository

Each Python script in this repository has the following structure:

```python
"""Lists  <--- Name of the topic here

# @see: https://www.learnpython.org/en/Lists  <-- Link to further readings goes here

Here might go more detailed explanation of the current topic (i.e. general info about Lists).
"""


def test_list_type():
    """Explanation of sub-topic goes here.

    Each file contains test functions that illustrate sub-topics (i.e. lists type, lists methods).
    """

    # Here is an example of how to build a list.  <-- Comments here explain the action
    squares = [1, 4, 9, 16, 25]

    # Lists can be indexed and sliced.
    # Indexing returns the item.
    assert squares[0] == 1  # <-- Assertions here illustrate the result.
    # Slicing returns a new list.
    assert squares[-3:] == [9, 16, 25]  # <-- Assertions here illustrate the result.
```

So normally you might want to do the following:

- [Find the topic](#table-of-contents) you want to learn or recap.
- Read comments and/or documentation that is linked in each script's docstring (as in example above).
- Look at code examples and assertions to see usage examples and expected output.
- Change code or add new assertions to see how things work.
- [Run tests](#testing-the-code) and [lint the code](#linting-the-code) to see if it work and is
written correctly.

## Table of Contents

1. **Getting Started**
    - [What is Python](src/getting_started/what_is_python.md)
    - [Python Syntax](src/getting_started/python_syntax.md)
    - [Variables](src/getting_started/test_variables.py)
2. **[Operators](src/operators/test_operators.py)**
3. **Data Types**
    - [Basic Types](src/data_types/test_basic_types.py)
    - [Lists](src/data_types/test_lists.py)
    - [Tuples and Sets](src/data_types/test_tuples.py)
    - [Dictionaries](src/data_types/test_dictionaries.py)
4. **[Control Flow](src/control_flow/test_control_flow.py)**
5. **Functions**
    - [Function Definition](src/functions/test_function_definition.py)
    - [Function Argument Possibilities](src/functions/test_arguments.py)
    - [Lambda Expressions](src/functions/test_lambda_expressions.py)
6. **Modules**
    - [Modules](src/modules/test_modules.py)
    - [Packages](src/modules/test_packages.py)
7. **[Exception Handling](src/exceptions/test_handle_exceptions.py)**
8. **Brief Tour of the Standard Libraries**
    - [Serialization](src/standard_libraries/test_json.py) (`json` library)
    - [String Pattern Matching](src/standard_libraries/test_re.py) (`re` library)
    - [Mathematics](src/standard_libraries/test_math.py) (`math`, `random`, `statistics` libraries)
    - [Dates and Times](src/standard_libraries/test_datetime.py) (`datetime` library)
9. **Additional Topics (further reading)**
    - [The `pass` statement](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
    - [Generators](https://docs.python.org/3/tutorial/classes.html#generators)
    - [Classes](https://docs.python.org/3/tutorial/classes.html)
10. **Exercise**
    - Process data from an API

## Prerequisites

**Installing Python**

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

You might want to use [venv](https://docs.python.org/3/library/venv.html) standard Python library
to create virtual environments and have Python, pip and all dependent packages to be installed and
served from the local project directory to avoid messing with system wide packages and their
versions.

Depending on your installation you might have access to Python3 interpreter either by
running `python` or `python3`. The same goes for pip package manager - it may be accessible either
by running `pip` or `pip3`.

You may check your Python version by running:

```bash
python --version
```

Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Installing dependencies**

Install all dependencies that are required for the project by running:

```bash
pip install -r requirements.txt
```

## Testing the Code

Tests are made using [pytest](https://docs.pytest.org/en/latest/) framework.

You may add new tests for yourself by adding files and functions with `test_` prefix
(i.e. `test_topic.py` with `def test_sub_topic()` function inside).

To run all the tests please execute the following command from the project root folder:

```bash
pytest
```

To run specific tests please execute:

```bash
pytest ./path/to/the/test_file.py
```

## Linting the Code

Linting is done using [pylint](http://pylint.pycqa.org/) and [flake8](http://flake8.pycqa.org/en/latest/) libraries.

### PyLint

To check if the code is written with respect
to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide please run:

```bash
pylint ./src/
```

In case the linter detects an error (i.e. `missing-docstring`) you may want
to read more about the specific error by running:

```bash
pylint --help-msg=missing-docstring
```

[More about PyLint](http://pylint.pycqa.org/)

### Flake8

To check if the code is written with respect
to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide please run:

```bash
flake8 ./src
```

Or if you want to have more detailed output you may run:

```bash
flake8 ./src --statistics --show-source --count
```

[More about Flake8](http://flake8.pycqa.org/en/latest/)

## Supporting the project

Many thanks to the original author [trekhleb](https://github.com/trekhleb).

You may support the **original** project via ❤️️ [GitHub](https://github.com/sponsors/trekhleb) or ❤️️ [Patreon](https://www.patreon.com/trekhleb).
