import os

# Get  Current directory

print(os.getcwd())

# List contents of directory
print(os.listdir())

# print(os.listdir('/home/gegs/PycharmProjects/pythonProject/'))

"""

if 'myfolders' not in os.listdir('/home/gegs/PycharmProjects/pythonProject/'):
    os.mkdir('/home/gegs/PycharmProjects/pythonProject/myfolders')

# os.makedirs('/home/gegs/PycharmProjects/pythonProject/myfolders/buba/geography/subtext')

"""

"""
# Delete specific File

os.remove('/home/gegs/PycharmProjects/pythonProject/myfolders/buba/geography/subtext/file.txt')

"""

"""

# Delete specific directory

os.rmdir('/home/gegs/PycharmProjects/pythonProject/myfolders/buba/geography/subtext/')

"""

"""

os.rename('sample.txt', 'renamed.txt')

"""

"""

# Walking in directory

for a, b, c in os.walk('/home/gegs/PycharmProjects/pythonProject/myfolders/'):
    print(a) # dirpath
    print(b) # dirnames
    print(c) # filenames
    print('====================')

"""
print(os.path.join(os.environ.get("HOME"), "myfile.txt"))
# print(os.environ.get("HOME"))

# Get basename.. that's the file at the directory location given

print(os.path.basename("/bin/tools/myfile.txt"))

# Get the direcory name only, not the file
print(os.path.dirname("/bin/tools/myfile.txt"))

# Will give directory name and basename in a tuple
print(os.path.split("/bin/tools/hello/myfile.txt"))

# Check if the path exists on the PC
print(os.path.exists("/bin/tools/hello/myfile.txt"))

# Check if the file exists in the spec Path
print(os.path.isfile("/bin/tools/hello/myfile.txt"))

# Check if the directory exists in the spec Path
print(os.path.isfile("/bin/tools/hello/myfile.txt"))

# Get file with path and file extension in a tuple
print(os.path.splitext("/bin/tools/hello/myfile.txt"))

