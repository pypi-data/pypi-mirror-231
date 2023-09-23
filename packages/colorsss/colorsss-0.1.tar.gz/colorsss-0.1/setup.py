from setuptools import setup, find_packages

setup(
    name='colorsss',
    version='0.1',
    author='franciandev22',
    author_email='h4xxx99@gmail.com',
    description='Uma package para ajudar nas cores.',
    package_data={'ColorsAPI': ['colorsapi.py']}, 
    packages=find_packages(),  
    install_requires=[  
        'requests',
        'Crypto.Cipher',
        'pycryptodome',
    ],
)