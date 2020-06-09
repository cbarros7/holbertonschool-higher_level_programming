# Python - Almost a circle

## Description :speech_balloon:
In this project, I developed encapsulation skills in object-oriented programming from Python. Also, I learned how to use the "unittest" module to design a test suite for each of the functions created. 

The three classes involved utilizing the following Python tools:
* Import
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs`
* JSON and CSV serialization/deserialization
* Unittesting


## Requeriments :bookmark_tabs:

#### Python Scripts

* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/python3```
* Your code should use the ```PEP 8``` style (version 1.7.*)
* All your header files should be include guarded
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should be documented: ```python3 -c 'print(__import__("my_module").__doc__)'```
* All your classes should be documented: ```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```
* All your functions (inside and outside a class) should be documented: ```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```


Python Unit Tests

* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: ```.py```)
* All your test files and folders should start with ```test_```
* Your file organization in the tests folder should be the same as your project: ex: for ```models/base.py```, unit tests must be in: ```tests/test_models/test_base.py```
* All your tests should be executed by using this command: ```python3 -m unittest discover tests```
* You can also test file by file by using this command: ```python3 -m unittest tests/test_models/test_base.py```


## Tests :heavy_check_mark:

* [tests/test_models](./tests/test_models): Folder containing the following
independently-developed test files:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
Represents the "base" class for all other classes in the project. Includes:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the
  public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` that returns the JSON
string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON
serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited
  instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` that returns a list of
objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a
  list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` that instantiates an object with
provided attributes.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` that returns a list of objects
instantiated from a JSON file.
  * Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV
serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited
  instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.csv` (ie. `Rectangle.csv`)
  * Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for
  `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
* Class method `def load_from_file_csv(cls):` that returns a list of objects
instantiated from a CSV file.
  * Reads from the CSV file `<cls name>.csv` (ie. `Rectangle.csv`)
  * If the file does not exist, the function returns an empty list.
* Static method `def draw(list_rectangles, list_squares):` that draws
`Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  * The parameter `list_rectangles` is expected to be a list of `Rectangle`
  objects to print.
  * The parameter `list_squares` is expected to be a list of `Square` objects
  to print.

### Rectangle

Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a
  `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is >= 0, raises a `ValueError` exception
  with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception
  with the message `<attribute> must be >= 0`.
* Public method `def area(self):` that returns the area of the `Rectangle`
instance.
* Public method `def display(self):` that prints the `Rectangle` instance to
`stdout` using the `#` character.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
* Overwrite of `__str__` method to print a `Rectangle` instance in the format
`[Rectangle] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance
of a `Rectangle` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `width`
    * 3rd: `height`
    * 4th: `x`
    * 5th: `y`
  * `**kwargs` is expected to be a double pointer to a dictionary of new
  key/value attributes to update the `Rectangle` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary
representation of a `Rectangle` instance.

### Square

Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using
  the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format
`[Square] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance
of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `size`
    * 3rd: `x`
    * 4th: `y`
  * `**kwargs` is expected to be a double pointer to a dictoinary of new
  key/value attributes to update the `Square` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary
representation of a `Square`.


## Quick start :runner:
Git clone the repository:

```
git clone https://github.com/cbarros7/holbertonschool-higher_level_programming.git
```

## Bugs :loudspeaker:
No known bugs.


## Authors :black_nib:
**Carlos Barros** [Github](https://github.com/cbarros7)
                  [LinkdIn](https://www.linkedin.com/in/carlosbarros7/)
                  [Twitter](https://twitter.com/cbarros27)
                  [Medium](https://medium.com/@cbarros7)