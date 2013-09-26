from setuptools import setup, find_packages

setup(
    name = "hipchatter",
    version = "1.0",
    url = 'http://github.com/tommymcglynn/hipchatter',
    license = 'Apache',
    description = "A sample project to help me understand how buildout works.",
    author = 'Tommy McGlynn',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)