from setuptools import find_packages, setup
# for test commit

setup(
    name='pythonparts',
    packages=find_packages(),
    version='1.0.0',
    description='PythonParts library',
    author='Yaroslav Oliinyk',
    license='Commercial Standard License',
    install_requires=['openpyxl==3.0.7',],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)
