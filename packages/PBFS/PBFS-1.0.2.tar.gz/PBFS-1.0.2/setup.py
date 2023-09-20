from setuptools import setup, find_packages


desc = "Performance Based Feature selection Technique: Prototype"

setup(
    name='PBFS',
    version='1.0.2',
    description= desc,
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url = 'https://github.com/hongzhu6129/HidenFeatures',
    author = 'Hong Zhu, Movin Fernandes',
    author_email= 'p0072431@brookes.ac.uk,movin.fernandes@hotmail.com',
    license='MIT',
    keywords=['Feature selection','Machine learning','Feature engineering','Performance based','open source'],
    packages=find_packages(),
    install_requires = '' ,
    include_package_data=True
)
