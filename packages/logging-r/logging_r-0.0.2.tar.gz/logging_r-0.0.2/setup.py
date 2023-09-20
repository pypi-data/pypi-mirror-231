from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'rotation logging'

# Setting up
setup(
    name="logging_r",
    version=VERSION,
    author="vector",
    author_email="<hmanshu94@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)