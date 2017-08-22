from setuptools import setup
import os

def readme():
  with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding="utf8") as f:
    return f.read()

setup(
  name='doctor_leipzig',
  version='1.0',
  description='Interlinear (Leipzig Rules) glossing for Markdown',
  long_description=readme(),
  url='https://github.com/parryc/doctor_leipzig',
  py_modules=['doctor_leipzig'],
  packages=['doctor_leipzig'],
  license='MIT',
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