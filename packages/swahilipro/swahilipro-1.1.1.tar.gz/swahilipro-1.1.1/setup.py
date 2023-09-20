from setuptools import setup, find_packages

setup(
    name='swahilipro',
    version='1.1.1',
    description='A compiler package',
    author='Masota & Ngigi',
    author_email='bonniemasota@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['swahilipro=swahilipro.shell:main']
    },
)
