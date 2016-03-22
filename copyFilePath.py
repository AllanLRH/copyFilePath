#!/usr/bin/env python
# -*- coding: utf8 -*-

###################################################################
# Copy absolute path of target file or folder if it exist.        #
# Absolute path is printet to stdout if `import pyperclip` fails. #
###################################################################

from __future__ import print_function  # For Python 2.7 backward compatability
import os
import sys
try:  # Place absolute path in clipboard if pyperclip module is installed
    import pyperclip
    returnAbsPath = lambda pth: pyperclip.copy(os.path.abspath(pth))
except ImportError:  # If not installed, print absolute path to stdout
    print('Pyperclip is not installed.',
          'The absolute path will be printet rather than placed in the clipboard.',
          file=sys.stderr, sep='\n')
    returnAbsPath = lambda pth: print(os.path.abspath(pth))

if len(sys.argv) != 2:
    print('Error, you must specify exactly one file or folder', file=sys.stderr)
    sys.exit(1)

userInput = os.path.expanduser(os.path.expandvars(sys.argv[1]))  # Expand paths
if os.path.exists(userInput):
    returnAbsPath(userInput)
else:
    print('Error, specified file or folder does not exist', file=sys.stderr)
    sys.exit(1)
