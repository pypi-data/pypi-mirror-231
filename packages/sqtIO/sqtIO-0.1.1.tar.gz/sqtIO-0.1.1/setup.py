from setuptools import setup, find_packages

setup(
    name='sqtIO',\
    version='0.1.1',\
    description='A package for handling SQT format ProLucid search files',\
    author='Prashanth Ciryam',\
    author_email='psciryam@gmail.com',\
    url='https://github.com/prashanthciryam/sqtIO', # Replace with your GitHub URL\
    packages=find_packages(),\
    install_requires=[
        'pandas>=1.0.0',\
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',\
        'Intended Audience :: Science/Research',\
        'License :: OSI Approved :: MIT License',\
        'Programming Language :: Python :: 3',\
        'Programming Language :: Python :: 3.6',\
        'Programming Language :: Python :: 3.7',\
        'Programming Language :: Python :: 3.8',\
        'Programming Language :: Python :: 3.9',\
        'Programming Language :: Python :: 3.10',\
        'Programming Language :: Python :: 3.11'
    ],
)
