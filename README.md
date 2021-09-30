[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/data-structures-and-algorithms/blob/main/LICENSE)
[![Tests](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/data-structures-and-algorithms/actions/workflows/tests.yml)

# data-structures-and-algorithms
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
To run tests: `python -m doctest -v */*.py`
