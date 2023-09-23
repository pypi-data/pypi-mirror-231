# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['parmap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-parmap',
    'version': '2.1.0',
    'description': 'Simple trivial parallelization',
    'long_description': None,
    'author': 'Fergal',
    'author_email': 'fergal.mullally@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)
