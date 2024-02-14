from setuptools import setup

setup(
    name='kiselev_ui_test_2024',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'pyqt5',
    ],
    entry_points='''
        [console_scripts]
        tate=main:main
    ''',
)