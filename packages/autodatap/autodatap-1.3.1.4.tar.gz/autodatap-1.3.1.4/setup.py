from setuptools import setup, find_packages

VERSION = '1.3.1.4'
DESCRIPTION = 'Automating Data Preprocessing'
LONGDESCRIPTION = """
# Automating Data Preprocessing
Shortly **ADP** is now a Python Library and you can use it by just installing using the following commands

```pip install autodatap```

And will install the package into you system

## Purpose of autodatap:

- to help you in data preprocessing

to know how can you use it:

- import the package

```import autodatap as adp```

### The main function in autodatap package is mainMethod so,

```adp.mainMethod("link to data set")```

and that's it, everything is done, you are good to go.

Now everything you will be doing will be in console (run)

## Currently supported funcitons

- Categorical Values (One-Hot-Encoding)

- Normalization

- Check for Imbalanced Data

- Null values finder and filling with 0 (in future with mean)

- dropping duplicate

## Licence

MIT License

Copyright (c) 2023 Syed Syab Ahmad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contribution

To contribute to the package follow the following link

https://github.com/SyabAhmad/Automating-Data-Preprocessing
"""
# Setting up
setup(
    name="autodatap",
    version=VERSION,
    author="SyabAhmad",
    description=DESCRIPTION,
    long_description=LONGDESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'scikit-learn'],  # Remove 'time'
    keywords=['python', 'machine learning', 'data science', 'data', 'preprocessing', 'AI'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'autodatap = autodatap.main:mainMethod',
        ],
    },
)
