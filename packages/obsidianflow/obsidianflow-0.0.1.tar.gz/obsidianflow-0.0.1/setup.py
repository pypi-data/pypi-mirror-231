'''
[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmcCJDViYmJkNDI2LTYxMGQtNDM5ZS05OTQ4LThhZDgzMDhiMWQxZQACKlszLCI1MDhiYzA3MC05NTgwLTQ3NTMtYjdiMC05MWE1M2QwZDBjYWUiXQAABiC6yE4wD4A0kBLTcwx5UKiyo8yfCGgGIP4Tu23TQGVGuQ
'''

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Supercharge your business with AI'
LONG_DESCRIPTION = 'A package that allows you to chat with your data'

# Setting up
setup(
    name="obsidianflow",
    version=VERSION,
    author="davnords",
    author_email="david.nordstromm@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'ai'],
)