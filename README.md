[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/data-structures-and-algorithms/blob/main/LICENSE)
[![Tests](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/tests.yml)
[![Lint](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/lint.yml)
[![Docs](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/docs.yml/badge.svg?branch=main)](https://onyonkaclifford.github.io/data-structures-and-algorithms)
[![imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![code style: flake8](https://img.shields.io/badge/code%20style-flake8-orange.svg)](https://github.com/pycqa/flake8)

Implementation of various data structures and algorithms

## Algorithms
An algorithm is a set of steps used to solve a problem. An example problem is the task of sorting a list of numbers in
ascending or descending order. The sequence of steps used to solve this problem forms an algorithm.

## Abstract data types
An abstract data type is a logical model that declares a set of high level operations that can be performed on data,
without specifying the implementation details. It provides an interface that describes the manipulation of data it
contains, from which a concrete implementation can be built upon.

An example of an abstract data type is the stack. It provides three main methods to manipulate data - push, pop, and
peek. It's concrete implementation may rely on an underlying list, array, or any other data structure to organise the
data held within itself.

## Data structures
A data structure is a concrete implementation of the organisation of data, and the set of operations that can be
performed on the data for efficient access and modification. It can be built based on the implementation of an abstract
data type, such as when implementing a stack using a list. It can also be built without relying on the logical model
presented by an abstract data type. An example is when the set of operations it can perform have a single implementation
detail.

Examples: array, doubly linked list.

## Tests
To run tests: `python -m doctest -v algorithms/**/*.py data_structures/**/*.py`

## Code formatting and styling
Isort, black and flake8 are used to format and style code. To automate this task, pre-commit hooks are used.

1. Install the pre-commit package: `pip install pre-commit`
2. Install git hook scripts: `pre-commit install`
3. (optional) Run against all the files: `pre-commit run --all-files`

The installed pre-commit hooks will automatically ensure use of a consistent code format and style whenever one commits
changes using git. For full documentation, view the [pre-commit docs](https://pre-commit.com/).
