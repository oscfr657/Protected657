#!/usr/bin/env python

from os import path

from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Protected657",
    version='0.2.1a',
    description='A Django app to keep files protected, works with Nginx.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oscar F',
    url='https://github.com/oscfr657/Protected657',
    packages=['protected657'],
    package_dir={'protected657': '.'},
    package_data={
        'protected657': [
            './migrations/*',
            './templates/*',
            './templates/*/*',
        ]
    },
    include_package_data=True,
    install_requires=[
        'django',
        'djangorestframework',
        'python-magic',
    ],
    license='Hippocratic License Version Number: 2.1 with Commons Clause License Condition v1.0',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
