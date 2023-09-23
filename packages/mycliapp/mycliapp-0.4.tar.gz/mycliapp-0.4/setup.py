from setuptools import setup, find_packages

setup(
    name='mycliapp',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'click',
        'databricks-sql-connector'
    ],
    entry_points={
        'console_scripts': [
            'mycliapp = mycliapp.main:hello',
        ],
    },
)
