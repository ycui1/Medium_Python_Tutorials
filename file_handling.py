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

from glob import glob
csv_files = glob('*.py')
for csv_file in csv_files:

    print(csv_file)
