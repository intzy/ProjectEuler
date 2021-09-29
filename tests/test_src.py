"""
Tests for Project Euler
"""

from importlib import import_module
from time import time

import pytest

from tests.solutions import SOLUTIONS


@pytest.mark.parametrize("problem_number", SOLUTIONS.keys())
def test_problem(problem_number):
    print("\n")
    mod = import_module("src.pb" + problem_number)
    func = getattr(mod, "problem" + problem_number)
    start_time = time()
    result = func()
    runtime = time() - start_time
    print("The result from Problem", problem_number, "is:", result)
    print("Elapsed time:", "%.6f" % runtime, "seconds.")
    assert result == SOLUTIONS[problem_number]
