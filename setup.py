try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An RSS Aggregator for Terminal to See Latest news.',
    'author': 'Buddy Lindsey',
    'url': 'http://buddylindsey.com',
    'download_url': '',
    'author_email': 'percent20@gmail.com',
    'version': '0.01',
    'install_requires': ['nose'],
    'packages': ['termnews'],
    'scripts': [],
    'name': 'termnews'
}
