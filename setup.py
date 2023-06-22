from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='genepass',
    version='0.1.2',
    author=' ny7777',
    author_email='meathouse47@gmail.com',
    url='https://github.com/senya-koku/genepass',
    description='genepass can automatically generates passwords',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    
    packages=find_packages()
)