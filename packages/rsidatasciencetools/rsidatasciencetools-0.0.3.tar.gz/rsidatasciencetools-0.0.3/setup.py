from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'RSI Data Science Tools'
LONG_DESCRIPTION = 'RSI Data Science Tools package'

# Setting up
setup(
        name="rsidatasciencetools", 
        version=VERSION,
        author="Gurinder Pal Singh",
        author_email="gpsingh@rsimail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],         
        keywords=['python', 'RSI Data Science Tools package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)