from setuptools import setup, find_packages

setup(
    name='mycliapp1',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'mycliapp1 = mycliapp.main:hello',
        ],
    },
)
