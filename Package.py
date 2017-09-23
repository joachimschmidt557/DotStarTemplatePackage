"""
The Package.py file contains all necessary information for
handling this package.

This python script will be called by DotStar when the user
decides to install, run or do something with the package.

Possible command-line arguments are:
    - "install"
        - "win.install"
    - "run"
        - "win.run"
    - "open"
    - "compile"
"""

import sys

def install_package():
    """
    This function contains all necessary information for
    installing the package
    """
    print("Test install")
    print("If you see this message, your DotStar is working!")

def run_package():
    """
    This function contains all necessary information for
    running the package
    """
    print("Test run")
    print("If you see this message, your DotStar is working!")

def compile_package():
    """
    This function contains all necessary information for
    compiling the package
    """
    print("Test compile")
    print("If you see this message, your DotStar is working!")


action = sys.argv[1]
if action == "install":
    install_package()
if action == "run":
    run_package()
if action == "compile":
    compile_package()
