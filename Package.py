"""
The Package.py file contains all necessary information for
handling this package.

This python script will be called by DotStar when the user
decides to install, run or do something with the package.

Possible command-line arguments are:
    - "install"
    - "run"
    - "open"
"""

import sys

def install_package():
    """
    This function contains all necessary information for
    installing the package
    """
    print("In installing")

def run_package():
    print("In run package")

action = sys.argv[1]
if action == "install":
    install_package()
if action == "run":
    run_package()
