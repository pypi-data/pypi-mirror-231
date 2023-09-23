from setuptools import setup, find_packages

VERSION = '1.2.4'
DESCRIPTION = 'Automating Data Preprocessing'

# Setting up
setup(
    name="autodatap",
    version=VERSION,
    author="SyabAhmad",
    description=DESCRIPTION,
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
