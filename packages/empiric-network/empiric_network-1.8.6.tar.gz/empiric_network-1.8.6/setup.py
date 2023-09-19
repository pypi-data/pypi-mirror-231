# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'empiric',
 'publisher': 'empiric/publisher',
 'publisher.fetchers': 'empiric/publisher/fetchers',
 'publisher.future_fetchers': 'empiric/publisher/future_fetchers',
 'test': 'empiric/test'}

packages = \
['core',
 'core.abis',
 'core.mixins',
 'empiric',
 'empiric.core',
 'empiric.core.abis',
 'empiric.core.mixins',
 'empiric.publisher',
 'empiric.publisher.fetchers',
 'empiric.publisher.future_fetchers',
 'empiric.test',
 'publisher',
 'publisher.fetchers',
 'publisher.future_fetchers',
 'test']

package_data = \
{'': ['*']}

install_requires = \
['cairo-lang>=0.12,<0.13', 'starknet.py==0.18.1', 'typer==0.6.1']

entry_points = \
{'console_scripts': ['interface-check = '
                     'empiric.test.interface_consistency:main']}

setup_kwargs = {
    'name': 'empiric-network',
    'version': '1.8.6',
    'description': 'Core package for rollup-native Pragma Oracle',
    'long_description': "# Empiric Network\n\n## About\n\nFor more information, see the [project's repository](https://github.com/Astraly-Labs/Empiric), [documentation overview](https://docs.empiric.network/) and [documentation on how to publish data](https://docs.empiric.network/using-empiric/publishing-data).\n",
    'author': 'Pragma',
    'author_email': 'contact@pragmaoracle.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pragmaoracle.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
