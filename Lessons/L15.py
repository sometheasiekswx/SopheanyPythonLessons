import os
import fnmatch

age = 15
name = 'tim'
location = 'somewhere'

print(name + " is " + str(age) + " years old. He lives in " + location)
print(f'{name} is {age} years old. He lives in {location}')

for rootDir, subdirs, filenames in os.walk('../F/'):
    for filename in filenames:
        if 'Copy' in filename:
            directory_to_remove = os.path.join(rootDir, filename)
            print(f'Removing {directory_to_remove} from Computer')
            os.remove(directory_to_remove)
