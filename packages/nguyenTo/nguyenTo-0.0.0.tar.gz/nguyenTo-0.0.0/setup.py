from setuptools import setup, find_packages

import codecs
import os
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding = "utf-8") as fh:
    long_description = "\n" + fh.read()
DESCRIPTION = 'python cho toán'

setup(
    name='nguyenTo',
    version='0.0.0',
    author="quanzui",
    author_email="<quan06122003@gmail.com>",
    description= DESCRIPTION,
    long_description_content_typr = "text/markdow",
    long_description= long_description,
    packages=find_packages(),
    keywords=['python','toán', 'prime'],
    classifiers=[
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: POSIX :: Linux",  
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
]

    
)
