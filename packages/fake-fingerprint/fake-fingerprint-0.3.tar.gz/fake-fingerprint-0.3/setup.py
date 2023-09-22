from setuptools import setup, find_packages

setup(
    name='fake-fingerprint',
    version='0.3',
    description='Receive good Fingerprints fast',
    author='Yokozuna',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'colorama',
    ],
)
