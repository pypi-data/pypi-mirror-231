from setuptools import setup

setup(
  name = "byte_words",
  version = "1.1.0",
  author = "John Baber-Lucero",
  author_email = "pypi@frundle.com",
  description = ("Turn binary files into words and vice versa"),
  license = "GPLv3",
  url = "https://github.com/jbaber/byte-words",
  packages = ['byte_words'],
  install_requires = [],
  tests_require=['pytest'],
  entry_points = {
    'console_scripts': ['byte-words=byte_words.byte_words:main'],
  }
)
