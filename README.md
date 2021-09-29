# Project Euler Solutions

The following are my solutions to some of the problems at [Project Euler](https://projecteuler.net/).
I believe that for many people, attempting the first 50 or so problems
is a good way to build up your algorithm design skills.
Some problems require nontrivial math to design a fast enough algorithm,
where as others require clever computer science techniques to
design a good algorithm.


## Problem Solutions

Most problems I solved using Python, though there are a few that I just using other tools
or pencil and paper.
For the problems I did solve using Python, my code is located in the `src` folder.
For none of my problems do I offer a step-by-step breakdown of my code.
Some of the problems, I offer a brief list of relevant mathematical or computer science
concepts that I use to solve the problem,
either in the module documentation, or in the comments section of the chart below.
If you are solving the problem, you can feel free to take these as hints.

## Usage

First, make sure that you have Python 3.9.7 or later installed.
If you use Python for much else,
it is then recommended you create a virtual environment.
I myself use [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
Once you are in your virtual environment, run
```
pip install -r requirements.txt
```
This installs all the required python packages.
To run a problem solutions, input
```python
python -m project_euler problem_number
```
where you replace `problem_number` with a three-digit string such as `045` or `148`.
If you want more accurate timing, you can run
```python
python -m project_euler -t [problem_number]
```
or
```python
python -m project_euler --timing [problem_number]
```
Note that it may take over a minute to calculate the running time when the timing flag is enabled.


## Timing Standards

For each of my solutions, I benchmark how long it takes to find the answer,
down to the millisecond.
There are a few problems where the solution takes much less than one millisecond,
in which case, I just list its running time as 0.000s.

For each problem, I try to choose an algorithm that will make the computation time fairly fast.
However, I don't micro-optimize my code to squeeze every last millisecond out of my solution.
Rather, after I have chosen my algorithm,
I prioritize making my code as clear and concise as possible.
Examples of where my code may not be the most optimal include
using list comprehensions in certain instances,
using lists instead of keeping a variable tally,
and splitting up my functions so many function calls are used.
If I wanted to get every last optimization out of my code,
I would have programmed in a language such as C or C++,
where one has much finer control over how your system will actually run your code.

Also, for problems where the input is given from a text file,
the run time includes reading from the text file.
For certain problems, reading from text makes up the bulk of the run time.

Most of my benchmarks we calculated using the module [timeit](https://docs.python.org/3/library/timeit.html).
More specifically, I first get a rough estimate of the running time by using Python's
[time](https://docs.python.org/3/library/time.html) module.
Once I get this estimate,
I use timeit to call a timer five times, each which runs my code <var>N</var> times,
where <var>N</var> is chosen so that each timer
takes approximately 12 seconds to complete.

Timing benchmarks are obtained
using CPython 3.9.7,
with a 2.2 GHz Quad-Core Intel Core i7,
on a MacOS version 11.6.

## List of Solved Problems

Below is a list of the problems I have solved, along with the running time of my code,
and my comments of some of the problems.
For problems where I give asymptotic bounds,
I assume basic arithmetic functions such as addition and multiplication takes constant time.


| Problem | Title                                                                      | Difficulty | Running Time (s) | Comments                                                                                                                              |
| ---     | ---                                                                        | ---        | ---              | ---                                                                                                                                   |
| 001     | [Multiples of 3 or 5](https://projecteuler.net/problem=001)                | 5%         | 0.000            | A constant time algorithm exists.                                                                                                     |
| 002     | [Even Fibonacci numbers](https://projecteuler.net/problem=002)             | 5%         | 0.000            |                                                                                                                                       |
| 003     | [Largest prime factor](https://projecteuler.net/problem=003)               | 5%         | 0.001            |                                                                                                                                       |
| 004     | [Largest palindrome product](https://projecteuler.net/problem=004)         | 5%         | 0.000            |                                                                                                                                       |
| 005     | [Smallest multiple](https://projecteuler.net/problem=005)                  | 5%         | 0.000            |                                                                                                                                       |
| 006     | [Sum square difference](https://projecteuler.net/problem=006)              | 5%         | 0.000            | A constant time algorithm exists.                                                                                                     |
| 007     | [10001st prime](https://projecteuler.net/problem=007)                      | 5%         | 0.009            | Sieve of Eratosthenes.                                                                                                                |
| 008     | [Largest product in a series](https://projecteuler.net/problem=008)        | 5%         | 0.001            | Running time includes reading from file.                                                                                              |
| 009     | [Special Pythagorean triplet](https://projecteuler.net/problem=009)        | 5%         | 0.000            | One can directly generate all Pythagorean triples.  Uniqueness is proven.                                                             |
| 010     | [Summation of primes](https://projecteuler.net/problem=010)                | 5%         | 0.186            | Sieve of Eratosthenes.                                                                                                                |
| 011     | [Largest product in a grid](https://projecteuler.net/problem=011)          | 5%         | 0.002            |                                                                                                                                       |
| 012     | [Highly divisible triangular number](https://projecteuler.net/problem=012) | 5%         | 0.026            | Recall that <var>n</var> and <var>n</var> + 1 are relatively prime.  In my algorithm, I don't assume any upper bound on <var>n</var>. |
| 013     | [Large sum](https://projecteuler.net/problem=013)                          | 5%         | 0.000            |                                                                                                                                       |
| 014     | [Longest Collatz sequence](https://projecteuler.net/problem=014)           | 5%         | 1.714            | Dynamic programming is almost essential.                                                                                              |
| 015     | [Lattice paths](https://projecteuler.net/problem=015)                      | 5%         | 0.000            | A combinatorical solution exists.                                                                                                     |
| 016     | [Power digit sum](https://projecteuler.net/problem=016)                    | 5%         | 0.000            |                                                                                                                                       |
| 017     | [Number letter counts](https://projecteuler.net/problem=017)               | 5%         | 0.001            |                                                                                                                                       |
| 018     | [Maximum path sum I](https://projecteuler.net/problem=018)                 | 5%         | 0.000            |                                                                                                                                       |
| 019     | [Counting Sundays](https://projecteuler.net/problem=019)                   | 5%         | 0.000            |                                                                                                                                       |
| 020     | [Factorial digit sum](https://projecteuler.net/problem=020)                | 5%         | 0.000            |                                                                                                                                       |
