from setuptools import setup, find_packages

setup(
    name='ytmp3-client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='ibra1410',
    description='Client library for YT-MP3 API',
    url='https://github.com/ibra1410/ytmp3',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
