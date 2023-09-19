from setuptools import setup, find_packages

setup(
    name = 'calc_basic_movin_v2',
    version = '0.0.1',
    description= 'Trial Basic calculator library',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url = '',
    author = 'Movin Fernandes',
    author_email= 'movin.fernandes@hotmail.com',
    license='MIT',
    keywords='basic',
    packages=find_packages(),
    install_requires = '' 
)