# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0.0'
long_description = '\n'.join([
        open("README.rst").read(),
        open("AUTHORS.rst").read(),
        open("HISTORY.rst").read(),
        ])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
    "Framework :: Sphinx",
    "Framework :: Sphinx :: Theme",
]

setup(
     name='sphinxjp.themes.sphinxjp',
     version=version,
     description='A sphinx theme for sphinx-users.jp site.',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['sphinx', 'reStructuredText', 'theme'],
     author='sphinx-users.jp',
     author_email='shimizukawa@gmail.com',
     url='https://github.com/sphinxjp/sphinxjp.themes.sphinxjp',
     license='MIT',
     namespace_packages=['sphinxjp', 'sphinxjp.themes'],
     packages=find_packages('.'),
     include_package_data=True,
     install_requires=[
        'setuptools',
        'sphinx',
     ],
     entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.sphinxjp:template_path
     """,
     zip_safe=False,
)

