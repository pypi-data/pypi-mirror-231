from setuptools import setup, find_packages

setup(
    name='swahilipro',
    version='1.1.2',
    description='A compiler package',
    author='Masota & Ngigi',
    author_email='bonniemasota@gmail.com',
    packages=['swahilipro'],
    entry_points={
        'console_scripts': ['swahilipro=swahilipro.shell:main']
    },
)
