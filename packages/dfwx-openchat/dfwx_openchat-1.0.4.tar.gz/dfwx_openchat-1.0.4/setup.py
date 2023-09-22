from setuptools import setup


setup(
    name='dfwx_openchat',
    version='1.0.4',
    description='A package for dfwx_openchat.',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    author='DavidTaylor1987',
    author_email='domainseller@foxmail.com',
    packages=['dfwx_openchat'],
    license='Apache License 2.0',
    install_requires=[
        'requests',
    ] 
)