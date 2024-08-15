# Whitebox: The library to perform Python white test
By [Marcelo de Jesús Núñez](mailto:mdjnunez9706@gmail.com)

## Description
Whitebox is a library that allows you to perform white test in Python with dinamic code.

With this library, you can test a string codebase with also a string test cases.
This library is useful to perform deeper test on code evaluation systems.

## Requirements:
- Python 3.11.1 or higher
- Poetry 1.8.3 or higher

## Usage
1. Clone this repo
2. Install the dependencies with `poetry install`
3. You can install the library by going to the repository folder and executing `pip3 install -e .`


## TestCase Format
Whitebox only accepts `TestCase` classes. So you have to use the standard `unittest` library from Python.
You don't have to import anything. Just call the function that you expect to receive on the codebase and whitebox will dinamically import the codebase function you mentioned before

Here's some example:

```python
class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operate('+', 2, 3), 5)
        self.assertEqual(operate('-', 1, 1), 0)
        self.assertEqual(operate('*', 0, 0), 0)
        self.assertEqual(operate('/', 4, 2), 2)

    def test_division_by_cero(self):
        self.assertEqual(operate('/', 4, 0), 0)
        self.assertEqual(operate('/', 0, 4), 0)
        self.assertEqual(operate('/', 0, 0), 0)
```

As you can see the `operate` function is not imported. Whitebox is the one that deals with it.


## Usage of the library
```python
from whitebox import whitebox

codebase = "" #Suppose this is the codebase
tests = "" #Suppose this is the result

result = whitebox(codebase, tests)
print(result)
"""
prints:
{
    "passed": True,
    "success_rate": 100.00,
}
"""
```

After you execute `whitebox` you will recive a dictionary with the following keys:
- `passed`: A boolean that indicates if all test case scenarios passed
-  `success_rate`: A float value with the success rate of test cases run