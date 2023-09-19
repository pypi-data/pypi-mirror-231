# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scope_capture']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'scope-capture',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'megahomyak',
    'author_email': 'g.megahomyak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
