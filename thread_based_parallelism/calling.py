import os
import sys

program = "python3"
print("Calling  process")
arguements = ['called.py']

os.execvp(program, (program, )+tuple(arguements))
print("Gone to calling process")