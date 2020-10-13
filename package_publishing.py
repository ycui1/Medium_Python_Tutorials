the_root_dir/
|-- README.md
|-- setup.py
|-- test_package
|   |-- __init__.py
|   |-- python_file_0.py
|   |-- python_file_1.py
|   |-- python_file_2.py


import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="test-package-username",
    version="0.1",
    author="Your Name",
    author_email="your_email",
    description="This is a test package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_github_page",
    packages=['test_package'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

the_root_dir/
|-- .eggs
|   |-- a bunch of files in this directory
|-- build
|   |-- a bunch of files in this directory
|-- dist
|   |-- test-package-username-0.1.tar.gz
|   |-- test_package_username-0.1-py3-none-any.whl
|-- test_package
|   |-- the original files in the package
|-- test_package_username.egg-info
|   |-- a bunch of files in this directory
|-- README.md
|-- setup.py
|-- test_package

from test_package import python_file_0

python_file_0.hello_world()