#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='aos',
    version='${version}',
    description=readme.partition('\n')[0],
    long_description=readme,
    author='sohu-movie',
    author_email='stevenlee87@126.com',
    url='https://github.com/stevenlee87/aos',
    packages=find_packages('aos'),
    package_dir={'': 'aos'},
    include_package_data=True,
    scripts=[
        'aos/manage.py'
    ],
    install_requires=[
        "django==1.7.0",
        "pillow",
        "gunicorn",
        "mysql-python",
        "django-jsonfield",
        "django-reversion",
        "django-crispy-forms",
        "django-xadmin==0.5.0",
        "django-autocomplete_light",
        "python-social-auth",
        "south",
        "raven",
        "gevent",
    ],
    entry_points={
        'console_scripts': [
            'aos = manage:main',
        ]
    },
)
