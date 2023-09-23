from setuptools import setup, find_packages

VERSION = '1.3.1.1'
DESCRIPTION = 'Automating Data Preprocessing'
LONGDESCRIPTION = """
# Automating Data Preprocessing
Shortly **ADP** is now a Python Library and you can use it by just installing using the following commands
```pip install autodatap```
And will install the package into you system
*Purpose of autodatap*:
- to help you in data preprocessing
to know how can you use it:
- import the package
```import autodatap as adp```
The main function in autodatap package is mainMethod so,
```adp.mainMethod("link to data set")```
and thats it, everything is done, you are good to go.
Now everything you will be doing will be in console (run)
Currently supported funcitons
- Categorical Values (One-Hot-Encoding)
- Normalization
- Check for Imbalanced Data
- Null values finder and filling with 0 (in future with mean)
- dropping duplicate
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
