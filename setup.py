from setuptools import setup, find_packages

readme = open('README.md').read()

VERSION = '0.1.6'



setup(
    name='genepass',
    version=VERSION,
    author=' ny7777',
    author_email='5938dai617@gmail.com',
    url='https://github.com/senya-koku/genepass',
    description='genepass can automatically generate (create) passwords',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    
    packages=find_packages()
)