from setuptools import setup, find_packages

setup(
    name='pde-tracker',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
    ],
)
