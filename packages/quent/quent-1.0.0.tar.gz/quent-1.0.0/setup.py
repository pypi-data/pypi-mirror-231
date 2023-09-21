from setuptools import setup, Extension


setup(ext_modules=[Extension(name='sequent', sources=['sequent/sequent.c'])])
