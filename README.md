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


| Problem | Title                                                                    | Difficulty | Running Time (s)                                                        |
| ---     | ---                                                                      | ---        | ---                                                                     |
| 001     | [Multiples of 3 or 5](projecteuler.net/problem=001)                      | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb001.py)   |
| 002     | [Even Fibonacci numbers](projecteuler.net/problem=002)                   | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb002.py)   |
| 003     | [Largest prime factor](projecteuler.net/problem=003)                     | 5%         | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb003.py)   |
| 004     | [Largest palindrome product](projecteuler.net/problem=004)               | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb004.py)   |
| 005     | [Smallest multiple](projecteuler.net/problem=005)                        | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb005.py)   |
| 006     | [Sum square difference](projecteuler.net/problem=006)                    | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb006.py)   |
| 007     | [10001st prime](projecteuler.net/problem=007)                            | 5%         | [0.009](github.com/intzy/ProjectEuler/blob/main/src/pb007.py)   |
| 008     | [Largest product in a series](projecteuler.net/problem=008)              | 5%         | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb008.py)   |
| 009     | [Special Pythagorean triplet](projecteuler.net/problem=009)              | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb009.py)   |
| 010     | [Summation of primes](projecteuler.net/problem=010)                      | 5%         | [0.186](github.com/intzy/ProjectEuler/blob/main/src/pb010.py)   |
| 011     | [Largest product in a grid](projecteuler.net/problem=011)                | 5%         | [0.002](github.com/intzy/ProjectEuler/blob/main/src/pb011.py)   |
| 012     | [Highly divisible triangular number](projecteuler.net/problem=012)       | 5%         | [0.025](github.com/intzy/ProjectEuler/blob/main/src/pb012.py)   |
| 013     | [Large sum](projecteuler.net/problem=013)                                | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb013.py)   |
| 014     | [Longest Collatz sequence](projecteuler.net/problem=014)                 | 5%         | [1.645](github.com/intzy/ProjectEuler/blob/main/src/pb014.py)   |
| 015     | [Lattice paths](projecteuler.net/problem=015)                            | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb015.py)   |
| 016     | [Power digit sum](projecteuler.net/problem=016)                          | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb016.py)   |
| 017     | [Number letter counts](projecteuler.net/problem=017)                     | 5%         | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb017.py)   |
| 018     | [Maximum path sum I](projecteuler.net/problem=018)                       | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb018.py)   |
| 019     | [Counting Sundays](projecteuler.net/problem=019)                         | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb019.py)   |
| 020     | [Factorial digit sum](projecteuler.net/problem=020)                      | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb020.py)   |
| 021     | [Amicable numbers](projecteuler.net/problem=021)                         | 5%         | [0.011](github.com/intzy/ProjectEuler/blob/main/src/pb021.py)   |
| 022     | [Names scores](projecteuler.net/problem=022)                             | 5%         | [0.008](github.com/intzy/ProjectEuler/blob/main/src/pb022.py)   |
| 023     | [Non-abundant sums](projecteuler.net/problem=023)                        | 5%         | [0.541](github.com/intzy/ProjectEuler/blob/main/src/pb023.py)   |
| 024     | [Lexicographic permutations](projecteuler.net/problem=024)               | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb024.py)   |
| 025     | [1000-digit Fibonacci number](projecteuler.net/problem=025)              | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb025.py)   |
| 026     | [Reciprocal cycles](projecteuler.net/problem=026)                        | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb026.py)   |
| 027     | [Quadratic primes](projecteuler.net/problem=027)                         | 5%         | [0.260](github.com/intzy/ProjectEuler/blob/main/src/pb027.py)   |
| 028     | [Number spiral diagonals](projecteuler.net/problem=028)                  | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb028.py)   |
| 029     | [Distinct powers](projecteuler.net/problem=029)                          | 5%         | [0.008](github.com/intzy/ProjectEuler/blob/main/src/pb029.py)   |
| 030     | [Digit fifth powers](projecteuler.net/problem=030)                       | 5%         | [0.018](github.com/intzy/ProjectEuler/blob/main/src/pb030.py)   |
| 031     | [Coin sums](projecteuler.net/problem=031)                                | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb031.py)   |
| 032     | [Pandigital products](projecteuler.net/problem=032)                      | 5%         | [0.060](github.com/intzy/ProjectEuler/blob/main/src/pb032.py)   |
| 033     | [Digit cancelling fractions](projecteuler.net/problem=033)               | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb033.py)   |
| 034     | [Digit factorials](projecteuler.net/problem=034)                         | 5%         | [3.020](github.com/intzy/ProjectEuler/blob/main/src/pb034.py)   |
| 035     | [Circular primes](projecteuler.net/problem=035)                          | 5%         | [0.231](github.com/intzy/ProjectEuler/blob/main/src/pb035.py)   |
| 036     | [Double-base palindromes](projecteuler.net/problem=036)                  | 5%         | [0.637](github.com/intzy/ProjectEuler/blob/main/src/pb036.py)   |
| 037     | [Truncatable primes](projecteuler.net/problem=037)                       | 5%         | [0.003](github.com/intzy/ProjectEuler/blob/main/src/pb037.py)   |
| 038     | [Pandigital multiples](projecteuler.net/problem=038)                     | 5%         | [0.028](github.com/intzy/ProjectEuler/blob/main/src/pb038.py)   |
| 039     | [Integer right triangles](projecteuler.net/problem=039)                  | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb039.py)   |
| 040     | [Champernowne's constant](projecteuler.net/problem=040)                  | 5%         | [1.470](github.com/intzy/ProjectEuler/blob/main/src/pb040.py)   |
| 041     | [Pandigital prime](projecteuler.net/problem=041)                         | 5%         | [0.827](github.com/intzy/ProjectEuler/blob/main/src/pb041.py)   |
| 042     | [Coded triangle numbers](projecteuler.net/problem=042)                   | 5%         | [0.003](github.com/intzy/ProjectEuler/blob/main/src/pb042.py)   |
| 043     | [Sub-string divisibility](projecteuler.net/problem=043)                  | 5%         | [3.299](github.com/intzy/ProjectEuler/blob/main/src/pb043.py)   |
| 044     | [Pentagon numbers](projecteuler.net/problem=044)                         | 5%         | [0.258](github.com/intzy/ProjectEuler/blob/main/src/pb044.py)   |
| 045     | [Triangular, pentagonal, and hexagonal](projecteuler.net/problem=045)    | 5%         | [0.026](github.com/intzy/ProjectEuler/blob/main/src/pb045.py)   |
| 046     | [Goldbach's other conjecture](projecteuler.net/problem=046)              | 5%         | [0.008](github.com/intzy/ProjectEuler/blob/main/src/pb046.py)   |
| 047     | [Distinct primes factors](projecteuler.net/problem=047)                  | 5%         | [0.204](github.com/intzy/ProjectEuler/blob/main/src/pb047.py)   |
| 048     | [Self powers](projecteuler.net/problem=048)                              | 5%         | [0.002](github.com/intzy/ProjectEuler/blob/main/src/pb048.py)   |
| 049     | [Prime permutations](projecteuler.net/problem=049)                       | 5%         | [0.333](github.com/intzy/ProjectEuler/blob/main/src/pb049.py)   |
| 050     | [Consecutive prime sum](projecteuler.net/problem=050)                    | 5%         | [0.087](github.com/intzy/ProjectEuler/blob/main/src/pb050.py)   |
| 051     | [Prime digit replacements](projecteuler.net/problem=051)                 | 15%        | [0.209](github.com/intzy/ProjectEuler/blob/main/src/pb051.py)   |
| 052     | [Permuted multiples](projecteuler.net/problem=052)                       | 5%         | [0.114](github.com/intzy/ProjectEuler/blob/main/src/pb052.py)   |
| 053     | [Combinatoric selections](projecteuler.net/problem=053)                  | 5%         | [0.010](github.com/intzy/ProjectEuler/blob/main/src/pb053.py)   |
| 054     | [Poker hands](projecteuler.net/problem=054)                              | 10%        | [0.031](github.com/intzy/ProjectEuler/blob/main/src/pb054.py)   |
| 055     | [Lychrel numbers](projecteuler.net/problem=055)                          | 5%         | [0.061](github.com/intzy/ProjectEuler/blob/main/src/pb055.py)   |
| 056     | [Powerful digit sum](projecteuler.net/problem=056)                       | 5%         | [0.253](github.com/intzy/ProjectEuler/blob/main/src/pb056.py)   |
| 057     | [Square root convergents](projecteuler.net/problem=057)                  | 5%         | [0.003](github.com/intzy/ProjectEuler/blob/main/src/pb057.py)   |
| 058     | [Spiral primes](projecteuler.net/problem=058)                            | 5%         | [3.026](github.com/intzy/ProjectEuler/blob/main/src/pb058.py)   |
| 059     | [XOR decryption](projecteuler.net/problem=059)                           | 5%         | [13.193](github.com/intzy/ProjectEuler/blob/main/src/pb059.py)  |
| 060     | [Prime pair sets](projecteuler.net/problem=060)                          | 20%        | [9.423](github.com/intzy/ProjectEuler/blob/main/src/pb060.py)   |
| 061     | [Cyclical figurate numbers](projecteuler.net/problem=061)                | 20%        | [0.171](github.com/intzy/ProjectEuler/blob/main/src/pb061.py)   |
| 062     | [Cubic permutations](projecteuler.net/problem=062)                       | 15%        | [0.031](github.com/intzy/ProjectEuler/blob/main/src/pb062.py)   |
| 063     | [Powerful digit counts](projecteuler.net/problem=063)                    | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb063.py)   |
| 064     | [Odd period square roots](projecteuler.net/problem=064)                  | 20%        | [0.441](github.com/intzy/ProjectEuler/blob/main/src/pb064.py)   |
| 065     | [Convergents of e](projecteuler.net/problem=065)                         | 15%        | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb065.py)   |
| 066     | [Diophantine equation](projecteuler.net/problem=066)                     | 25%        | [0.012](github.com/intzy/ProjectEuler/blob/main/src/pb066.py)   |
| 067     | [Maximum path sum II](projecteuler.net/problem=067)                      | 5%         | [0.003](github.com/intzy/ProjectEuler/blob/main/src/pb067.py)   |
| 068     | [Magic 5-gon ring](projecteuler.net/problem=068)                         | 25%        | [0.095](github.com/intzy/ProjectEuler/blob/main/src/pb068.py)   |
| 069     | [Totient maximum](projecteuler.net/problem=069)                          | 10%        | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb069.py)   |
| 070     | [Totient permutation](projecteuler.net/problem=070)                      | 20%        | [29.043](github.com/intzy/ProjectEuler/blob/main/src/pb070.py)  |
| 074     | [Digit factorial chains](projecteuler.net/problem=074)                   | 15%        | [2.149](github.com/intzy/ProjectEuler/blob/main/src/pb074.py)   |
| 075     | [Singular integer right triangles](projecteuler.net/problem=075)         | 25%        | [1.018](github.com/intzy/ProjectEuler/blob/main/src/pb075.py)   |
| 076     | [Counting summations](projecteuler.net/problem=076)                      | 10%        | [0.004](github.com/intzy/ProjectEuler/blob/main/src/pb076.py)   |
| 077     | [Prime summations](projecteuler.net/problem=077)                         | 25%        | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb077.py)   |
| 078     | [Coin partitions](projecteuler.net/problem=078)                          | 30%        | [3.623](github.com/intzy/ProjectEuler/blob/main/src/pb078.py)   |
| 079     | [Passcode derivation](projecteuler.net/problem=079)                      | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb079.py)   |
| 080     | [Square root digital expansion](projecteuler.net/problem=080)            | 20%        | [0.002](github.com/intzy/ProjectEuler/blob/main/src/pb080.py)   |
| 090     | [Cube digit pairs](projecteuler.net/problem=090)                         | 40%        | [0.014](github.com/intzy/ProjectEuler/blob/main/src/pb090.py)   |
| 091     | [Right triangles with integer coordinates](projecteuler.net/problem=091) | 25%        | [2.923](github.com/intzy/ProjectEuler/blob/main/src/pb091.py)   |
| 092     | [Square digit chains](projecteuler.net/problem=092)                      | 5%         | [0.035](github.com/intzy/ProjectEuler/blob/main/src/pb092.py)   |
| 093     | [Arithmetic expressions](projecteuler.net/problem=093)                   | 35%        | [0.412](github.com/intzy/ProjectEuler/blob/main/src/pb093.py)   |
| 095     | [Amicable chains](projecteuler.net/problem=095)                          | 30%        | [5.750](github.com/intzy/ProjectEuler/blob/main/src/pb095.py)   |
| 096     | [Su Doku](projecteuler.net/problem=096)                                  | 25%        | [8.984](github.com/intzy/ProjectEuler/blob/main/src/pb096.py)   |
| 097     | [Large non-Mersenne prime](projecteuler.net/problem=097)                 | 5%         | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb097.py)   |
| 098     | [Anagramic squares](projecteuler.net/problem=098)                        | 35%        | [0.257](github.com/intzy/ProjectEuler/blob/main/src/pb098.py)   |
| 099     | [Largest exponential](projecteuler.net/problem=099)                      | 10%        | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb099.py)   |
| 103     | [Special subset sums: optimum](projecteuler.net/problem=103)             | 45%        | [102.860](github.com/intzy/ProjectEuler/blob/main/src/pb103.py) |
| 105     | [Special subset sums: testing](projecteuler.net/problem=105)             | 45%        | [0.22](github.com/intzy/ProjectEuler/blob/main/src/pb105.py)    |
| 118     | [Pandigital prime sets](projecteuler.net/problem=118)                    | 45%        | [29.814](github.com/intzy/ProjectEuler/blob/main/src/pb118.py)  |
| 123     | [Prime square remainders](projecteuler.net/problem=123)                  | 30%        | [0.140](github.com/intzy/ProjectEuler/blob/main/src/pb118.py)   |
| 129     | [Repunit divisibility](projecteuler.net/problem=129)                     | 45%        | [0.318](github.com/intzy/ProjectEuler/blob/main/src/pb129.py)   |
| 130     | [Composites with prime repunit property](projecteuler.net/problem=130)   | 45%        | [1.094](github.com/intzy/ProjectEuler/blob/main/src/pb130.py)   |
| 131     | [Prime cube partnership](projecteuler.net/problem=131)                   | 40%        | [0.004](github.com/intzy/ProjectEuler/blob/main/src/pb131.py)   |
| 137     | [Fibonacci golden nuggets](projecteuler.net/problem=137)                 | 50%        | [1.237](github.com/intzy/ProjectEuler/blob/main/src/pb137.py)   |
| 140     | [Modified Fibonacci golden nuggets](projecteuler.net/problem=140)        | 55%        | [0.001](github.com/intzy/ProjectEuler/blob/main/src/pb140.py)   |
| 146     | [Investigating a Prime Pattern](projecteuler.net/problem=146)            | 50%        | [37.834](github.com/intzy/ProjectEuler/blob/main/src/pb146.py)  |
| 491     | [Double pandigital number divisible by 11](projecteuler.net/problem=491) | 20%        | [0.028](github.com/intzy/ProjectEuler/blob/main/src/pb491.py)   |
| 493     | [Under The Rainbow](projecteuler.net/problem=493)                        | 10%        | [0.000](github.com/intzy/ProjectEuler/blob/main/src/pb493.py)   |
| 500     | [Problem 500!!!](projecteuler.net/problem=500)                           | 15%        | [1.211](github.com/intzy/ProjectEuler/blob/main/src/pb500.py)   |
| 719     | [Number Splitting](projecteuler.net/problem=719)                         | 5%         | [15.616](github.com/intzy/ProjectEuler/blob/main/src/pb719.py)  |
