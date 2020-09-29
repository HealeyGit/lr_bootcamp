import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lr_bootcamp',
    version='0.0.1',
    author='Luke Remage-Healey',
    author_email='healey@cns.umass.edu',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
