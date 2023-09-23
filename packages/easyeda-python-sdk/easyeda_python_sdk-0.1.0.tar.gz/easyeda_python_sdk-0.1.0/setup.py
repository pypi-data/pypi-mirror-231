# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easyeda', 'easyeda.core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easyeda-python-sdk',
    'version': '0.1.0',
    'description': 'Python SDK for easyeda',
    'long_description': '',
    'author': 'Thomas Mahé',
    'author_email': 'contact@tmahe.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
