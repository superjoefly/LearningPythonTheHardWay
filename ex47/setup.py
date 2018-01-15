try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = [
    'description': 'LPHW Exercise 47',
    'author': 'JoeFly',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'newitup@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
]

setup(**config)
