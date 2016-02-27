try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Python units converter',
        'author': 'Aldo Sotolongo',
        'author_email': 'aldenso@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['pyconverter'],
        'scripts': [],
        'name': 'pyconverter'
        }

setup(**config)
