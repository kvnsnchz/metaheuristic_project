
SHO — Stochastic Heuristics Optimization
########################################

SHO is a didactic Python framework for implementing metaheuristics
(or evolutionary computation, or search heuristics).

Its main objective is to free students from implementing boring stuff
and allow them to concentrate on single operator implementation.

The framework implements a simple sensor placement problem
and handle metaheuristics manipulating solutions represented as
numerical vectors or bitstrings.

Executable
==========

The main interface is implemented in `snp.py`.
New algorithms should be integrated within this file and the interface should not be modified.
One may add arguments, but not remove or change the contracts of the existing ones.

The file `snp_landscape.py` is an example that plots the objective function
and a greedy search trajectory for a simple problem with only two dimensions.


Architecture
============

The design pattern of the framework is a functional approach to composition.
The goal is to be able to assemble a metaheuristic, by plugging atomic
functions in an algorithm template.

Operators
---------

The base of the pattern is a function that contains the main loop
of the algorithm, and call other functions called "operators".
Example of those algorithms are in the `algo` module.

For instance, the `random` algorithm depends on an objective function `func`,
an initialization operator `init` and a stopping criterion operator `again`.

Encoding
--------

Some operator do not depend on the way solutions are encoded
(like the stopping criterions) and some operators do depend on the encoding.
The former are defined in their own modules while the later are defined
in the module corresponding to their encoding (either `num` or `bit`).


Interface capture
-----------------

As they are assembled in an algorithm that do not know their internal
in advance, an operators needs to honor an interface.
For instance, the `init` operator's interface takes no input parameter
and returns a solution to the problem.

However, some operator may need additional parameters to be passed.
To solve this problem, the framework use an interface capture pattern,
implemented in the `make` module.
Basically, a function in this module capture the operator function's full
interface and returns a function having the expected interface of the
operator.

The implicit rule is to use positional arguments for mandatory parameters
on which the operator is defined, and keyword arguments for parameters
which are specific to the operator.

Exercises
=========

Setup
-----

To setup your own solver, first copy the `snp.py` file and rename it
with your name, for instance `dreo.py`.
You will then add your algorithm(s) into this executable.

Two example algorithms are provided: a `random` search
and a `greedy` search.
Several useful stopping criterions are provided.
The corresponding encoding-dependent operators are also provided,
for both numeric and bitstring encodings.
The `snp.py` file shows how to assemble either a numeric greedy solver
or a bitstring greedy solver.


Implement a simulated annealing
-------------------------------

Implement an evolutionary algorithm
-----------------------------------

Implement an expected run time empirical cumulative density function
------------------------------------------------------------------

