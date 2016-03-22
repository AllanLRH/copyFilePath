# copyFilePath

## Description
Takes exactly one file or folder as input.
If input exists, the absolute path of the input is placed in the clipboard, provided that the python module _pyperclip_ is installed, otherwise the absolute path is printed to stdout.

If for some reason you don't want to install pyperclip, you could just use the terminal clipboard function of your OS.
On mac it's called `pbcopy`, so a convenient alias this program could be
`alias cfp='/path/to/copyFilePath.py | pbcopy'`.

## Compatibility
Tested on Mac OS X Yosemite 10.10.5 with Python 2.7.11 and 3.5.1.
