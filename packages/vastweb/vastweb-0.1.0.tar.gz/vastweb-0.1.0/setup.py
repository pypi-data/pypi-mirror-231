
### `setup.py`:


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vastweb',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['Flask'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your_username/vastweb',
    license='MIT',
    description='A module for simplifying web development with Flask.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
