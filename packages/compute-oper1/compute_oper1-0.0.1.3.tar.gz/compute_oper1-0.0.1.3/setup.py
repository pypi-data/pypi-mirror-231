from setuptools import setup, find_packages

setup(
    name = 'compute_oper1',
    version = '0.0.1.3',
    description= 'Trial Basic calculator library, individual functions',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url = 'https://github.com/hongzhu6129/HidenFeatures',
    author = 'Movin Fernandes',
    author_email= 'movin.fernandes@hotmail.com',
    license='MIT',
    keywords=['basic','calculator'],
    packages=find_packages(),
    install_requires = '' ,
    include_package_data=True
)