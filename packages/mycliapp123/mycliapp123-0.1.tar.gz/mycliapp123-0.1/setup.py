from setuptools import setup, find_packages

setup(
    name='mycliapp123',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'databricks-sql-connector'
    ],
    entry_points={
        'console_scripts': [
            'mycliapp123 = mycliapp.main:hello',
        ],
    },
)
