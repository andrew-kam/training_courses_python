import os
import os.path
import shutil

print(os.getcwd())
print(os.listdir())
print(os.listdir('tests'))
print(os.path.exists('.idea'))
print(os.path.exists('lst.py'))
print()
print(os.path.isfile('lst.py'))
print(os.path.isdir('tests'))
print(os.path.abspath('lst.py'))
# os.chdir('tests') # change dir
# print(os.getcwd())
print()
shutil.copy("tests/test1.txt", "tests/test11.txt") # copy file from ... to ...
#shutil.copytree("tests", "tests/tests") # copy folder from ... to ...

for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)
