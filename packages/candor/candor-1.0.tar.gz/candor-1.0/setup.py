from setuptools import setup, find_packages

setup(
    name='candor',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    author='FroostySnoowman',
    author_email='froostysnoowmanbusiness@gmail.com',
    description='Python Library for Candor Services\' Project Mercury API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/candorservices/candor-py',
)