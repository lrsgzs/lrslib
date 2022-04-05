# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="lrslib",
    version="1.0.0",
    description="这是lrslib",
    long_description="README.md",
    long_description_content_type='text/markdown',
    author="Lrs",
    author_email="liurongshuo2022@outlook.com",
    url="http://github.com/lrsgzs/lrslib",
    packages=find_packages(),
    install_requires=['pygame','pillow'],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)