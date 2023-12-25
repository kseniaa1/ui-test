from setuptools import setup, find_packages

setup(
    name='calculator_package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'calculator_app = calculator.calculator_app:main'
        ]
    }
)