#!/usr/bin/env python3
"""Randomized CS 253 tracing-problem generator.

Usage:
    python3 cs253_problem_generator.py --topic rb --seed 42 --with-solution > problem.tex
    python3 cs253_problem_generator.py --list-topics
    python3 cs253_problem_generator.py --write-all output

The generators live in the problemgen package; see problemgen/__init__.py.
"""

from problemgen.cli import main

if __name__ == "__main__":
    main()
