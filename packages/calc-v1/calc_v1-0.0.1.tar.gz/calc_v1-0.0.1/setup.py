from setuptools import setup, find_packages

setup(
    name = 'calc_v1',
    version = '0.0.1',
    description= 'Trial Basic calculator library, individual functions',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url = '',
    author = 'Movin Fernandes',
    author_email= 'movin.fernandes@hotmail.com',
    license='MIT',
    keywords=['basic','calculator'],
    packages=find_packages(),
    install_requires = '' 
)