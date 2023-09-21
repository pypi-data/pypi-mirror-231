from setuptools import setup, find_packages

setup(
    name='UnBIASing',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    'pandas',
    'transformers',
    'torch',
    'sentencepiece'
     ],

     package_data={
        'unbias': ['data/*'],
    },
    author='Shaina Raza',
    author_email='shaina.raza@utoronto.ca',
    description='A package to detect and debias text using pretrained models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_github_username/UnBIASing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
