# To find out the current work directory
import os
print("Current Work Directory:", os.getcwd())
# Alternatively, we can use the pathlib
from pathlib import Path
print("Current Work Directory:", Path.cwd())

# Create a new directory in the current directory
os.mkdir("test_folder")
print("Is the directory there:", os.path.exists("test_folder"))
# Create a new directory in the specified directory
os.mkdir('/Users/ycui1/PycharmProjects/tmp_folder')
print("Is the directory there:", os.path.exists('/Users/ycui1/PycharmProjects/tmp_folder'))

# Create a new directory with subdirectories
os.makedirs('tmp_level0/tmp_level1')
print("Is the directory there:", os.path.exists("tmp_level0/tmp_level1"))

# Use the pathlib
from pathlib import Path
Path("test_folder").mkdir(parents=True, exist_ok=True)

txt_files = list(Path('.').glob("*.txt"))
print("Txt files:", txt_files)

from glob import glob
files = list(glob('h*'))
print("Files starting with h:", files)

target_folder = Path("target_folder")
target_folder.mkdir(parents=True,exist_ok=True)
source_folder = Path('.')

txt_files = source_folder.glob('*.txt')
for txt_file in txt_files:
    filename = txt_file.name
    target_path = target_folder.joinpath(filename)
    print(f"** Moving file {filename}")
    print("Target File Exists:", target_path.exists())
    txt_file.rename(target_path)
    print("Target File Exists:", target_path.exists(), '\n')


import shutil

source_file = "hello.txt"
target_file = "hello2.txt"
target_file_path = Path(target_file)
print("* Before copying, file exists:", target_file_path.exists())
shutil.copy(source_file, target_file)
print("* After copying, file exists:", target_file_path.exists())


for py_file in Path().glob('c*.py'):
    print('Name with extension:', py_file.name)
    print('Name only:', py_file.stem)

file_path = Path('closures.py')
print("File Extension:", file_path.suffix)

# Get the st_stat object from the path
current_file_path = Path('iterable_usages.py')
file_stat = current_file_path.stat()
# Get the file size:
print("File Size in Bytes:", file_stat.st_size)
# Get the time of most recent access
print("When Most Recent Access:", file_stat.st_atime)
# Get the time of most recent content modification
print("When Most Recent Modification:", file_stat.st_mtime)

# Read all the texts
with open("hello2.txt", 'r') as file:
    print(file.read())

# Read line by line
with open("hello2.txt", 'r') as file:
    for i, line in enumerate(file, 1):
        print(f"* Reading line #{i}: {line}")

# Write new data to the file
with open("hello3.txt", 'w') as file:
    text_to_write = "Hello Files From Writing"
    file.write(text_to_write)

# Append some data
with open("hello3.txt", 'a') as file:
    text_to_write = "\nHello Files From Appending"
    file.write(text_to_write)

# Check if the file has the correct data
with open("hello3.txt") as file:
    print(file.read())

# Delete a file
print(f"* Before deleting file {os.path.isfile('tmp.txt')}")
os.remove('tmp.txt')
print(f"* After deleting file {os.path.exists('tmp.txt')}")

# Delete a directory
print(f"* Before deleting directory {os.path.isdir('tmp_folder')}")
os.rmdir('tmp_folder')
print(f"* After deleting directory {os.path.exists('tmp_folder')}")

from zipfile import ZipFile

# To create a zip file that includes all the text files in the directory
with ZipFile('text_files.zip', 'w') as file:
    for txt_file in Path().glob('*.txt'):
        print(f"*Add file: {txt_file.name} to the zip file")
        file.write(txt_file)


# To unzip a file that is just created
with ZipFile('text_files.zip') as zip_file:
    zip_file.printdir()
    zip_file.extractall()

# To use the exists() in the os module
os.path.exists('path_to_check')

# To use the exists() in the pathlib module
Path('directory_path').exists()

# To check if a path is a directory
os.path.isdir('path_to_check')
Path('path_to_check').is_dir()

# To check if a path is a file
os.path.isfile('path_to_check')
Path('path_to_check').is_file()