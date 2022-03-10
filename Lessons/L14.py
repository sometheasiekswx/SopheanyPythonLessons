import os
from re import search

with os.scandir('../F/') as folder:
    for item in folder:
        if item.is_file():
            filename = item.name
            if search('Copy', filename):
                print('Removing ' + item.path)
                os.remove(item.path)
