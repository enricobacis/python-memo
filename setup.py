from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='python-memo',
      version='0.1.0',
      description='Decorators to memoize function results (also for classes)',
      long_description=long_description,
      url='http://github.com/enricobacis/python-memo',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['memo'],
      keywords='memo memoize dynamic programming cache decorator instance'
)
