from setuptools import setup
import os

setup(
  name='doctor_leipzig',
  version='1.1',
  description='Interlinear (Leipzig Rules) glossing for Markdown',
  long_description='Doctor Lepizig is a set of additional Markdown syntax items that help with constructing interlinear glosses within Markdown pages. Please see the README or website for full API.',
  url='https://github.com/parryc/doctor_leipzig',
  py_modules=['doctor_leipzig'],
  packages=['doctor_leipzig'],
  license='MIT',
  author='parryc',
  author_email='parry@parryc.com',
  keywords='interlinear leipzig glossing gloss markdown',
  install_requires=['markdown>=2.5'],
  classifiers=[
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: Markup :: HTML'
    ]
)