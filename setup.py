import versioneer
from setuptools import setup, find_packages

setup(name='prednet',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='Not open source',
      packages=find_packages(),
      )
