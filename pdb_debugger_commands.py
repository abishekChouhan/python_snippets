### To invoke debugger (pdb.py) in the interpretter:
# python -m pdb myscript.py
### Then use debugger commands

### Or can insert:
# import pdb
# pdb.set_trace()
### at the location you want to break into debugger.


### Commands:
# h : help
# n           : execute next line
# c           : complete execution
# l           : list 3 lines before and after current line
# s           : step into function call
# b           : show list of all break points
# b[int]      : set break point at line number (eg. b10)
# b [func]    : break at function name
# cl          : clear all break point
# cl[int]     : clear break point at line number
# p           : print

# Note: Use pudb package for semi-graphical debugger.
# pip install pudb
