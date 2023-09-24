import sys

# check must be located before importing code that uses 3.10 features
if sys.version_info < (3, 10):
    exit("Error: Python version 3.10 or higher is required.")

from dotcoder.app import run_cli

# This is only here so that dotcoder can be run with python -m dotcoder
# This file will NOT run when run from pip installation
run_cli()
