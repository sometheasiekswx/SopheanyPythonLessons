import os
import math
import re


with open('L1.py', 'r') as code_file:
    print(code_file.read())

with open('L1.py', 'a') as code_file:
    print(code_file.write('This is good code'))

delete_text = '../F/New Text Document.txt'
if os.path.exists(delete_text):
    os.remove(delete_text)
else:
    print("The file does not exist")
