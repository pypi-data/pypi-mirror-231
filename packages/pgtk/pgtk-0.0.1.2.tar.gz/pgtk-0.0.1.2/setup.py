from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    readme = file.read()

setup(
    name='pgtk',
    version='0.0.1.2',
    license='MIT license',
    author='Vinicius Putti Morais',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='viniputtim@gmail.com',
    keywords='pygame',
    description='Provides some simple functionalities using pygame',
    packages=find_packages(),
    install_requires=['pygame']
)
