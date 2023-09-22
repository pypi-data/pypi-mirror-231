from setuptools import setup

setup(
    name='aiiiSharedPython',
    version='0.0.8',
    description='Aiii Shared Package',
    author='Ranger',
    author_email='ranger1214v@gmail.com',
    url='https://github.com/ranger1214v/aiii-shared-python',
    packages=['aiiiSharedPython'],
    install_requires=[
        'requests',
    ],
    tests_require=['pytest', 'pytest-cov'],
)