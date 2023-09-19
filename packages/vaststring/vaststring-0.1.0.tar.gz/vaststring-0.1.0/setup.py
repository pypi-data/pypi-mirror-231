from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vaststring',
    version='0.1.0',
    packages=['vaststring'],
    install_requires=[],  # Add any dependencies here
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your_username/vaststring',
    license='MIT',
    description='A collection of advanced string manipulation functions for Python.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
