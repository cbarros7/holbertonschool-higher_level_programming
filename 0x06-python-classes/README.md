# 0x06. Python - Classes and Objects :robot:

## Description :speech_balloon:
In this project, I began practicing object-oriented programming using ```classes``` and ```objects``` in Python. I learned about ```attributes```, ```methods```, and properties as well as ```data abstraction```, ```data encapsulation```, and ```information hiding```.

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


## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Tasks :page_with_curl:

* **0. My first square**
  * [0-square.py](./0-square.py): Python class `Square` that defines a square.

* **1. Square with size**
  * [1-square.py](./1-square.py): Python class `Square` that defines a square. Builds on
  [0-square.py](./0-square.py) with:
    * Private instance attribute `size`.
    * Instantiation with `size`.

* **2. Size validation**
  * [2-square.py](./2-square.py): Python class `Square` that defines a square. Builds on
  [1-square.py](./1-square.py) with:
    * Instantiation with optional `size`: `def __init__(self, size=0):`
  * If a provided `size` attribute is not an integer, a `TypeError` exception
  is raised with the message `must be an integer`.
  * If a provided `size` attribute is less than `0`, a `ValueError` exception
  is raised with the message `size must be >= 0`.

* **3. Area of a square**
  * [3-square.py](./3-square.py): Python class `Square` that defines a square. Builds on
  [2-square.py](./2-square.py) with:
    * Public instance attribute `def area(self):` that returns the current
    square area.

* **4. Access and update private attribute**
  * [4-square.py](./4-square.py): Python class `Square` that defines a square. Builds on
  [3-square.py](./3-square.py) with:
    * Property `def size(self):` to retrieve the private instance
    attribute `self`.
    * Property setter `def size(self, value):` to set `self`.

* **5. Printing a square**
  * [5-square.py](./5-square.py): Python class `Square` that defines a square. Builds on
  [4-square.py](./4-square.py) with:
    * Public instance method `def my_print(self):` that prints the square
    with the character `#` to standard output (if `size` == 0 -> prints an empty
    line).

* **6. Coordinates of a square**
  * [6-square.py](./6-square.py): Python class `Square` that defines a square. Builds on
  [5-square.py](./5-square.py) with:
    * Private instance attribute `position`.
    * Property `def position(self):` to retreive `position`.
    * Property setter `def position(self, value):` to set `position`.
    * Instantiation with optional `size` and `position`:
    `def __init__(self, size=0, position=(0, 0)):`
  * If a provided `position` attribute is not a tuple of two integers, a
  `TypeError` exception is raised with the message `position must be a tuple of
  2 positive integers`.


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
