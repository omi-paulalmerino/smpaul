from setuptools import setup

NAME = "smpaul"
VERSION = "0.1.1"

REQUIRES = [
  "requests",
]

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name=NAME,
    version=VERSION,    
    description=""" The description of the package   """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omi-paulalmerino/smpaul",
    author="Paul Almerino",
    author_email="paul.almerino@smsupermalls.com",
    license="BSD 2-clause",
    packages=[NAME],
    install_requires=REQUIRES,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)