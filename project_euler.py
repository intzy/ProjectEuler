"""
Main file for Project Euler
"""

import argparse
import timeit
from importlib import import_module
from time import time

REPEATS = 5


def main():
    parser = argparse.ArgumentParser()
    help_string = """
    Calculate the solution's runtime with increased accuracy.
    Note that with this option enabled,
    calculating the runtime can take over a minute to complete.
    """
    parser.add_argument(
        "-t",
        "--timing",
        help=help_string,
        action="store_true",
    )
    parser.add_argument(
        "problem_number", help='Three digit problem code, such as "045" or "148".'
    )
    args = parser.parse_args()
    project_euler(args.problem_number, args.timing)


def project_euler(problem_number, accurate_timing):
    print()
    try:
        mod = import_module("src.pb" + problem_number)
    except ModuleNotFoundError:
        print("Problem", problem_number, "not yet implemented.")
        return
    func = getattr(mod, "problem" + problem_number)
    start_time = time()
    result = func()
    runtime = time() - start_time
    print("The result from Problem", problem_number, "is:", result)
    if accurate_timing:
        n = int(60 / (REPEATS * runtime)) + 1
        runtime = min(timeit.Timer(func).repeat(repeat=REPEATS, number=n)) / n
    print("Runtime:", "%.6f" % runtime, "seconds.")
    print()


if __name__ == "__main__":
    main()
